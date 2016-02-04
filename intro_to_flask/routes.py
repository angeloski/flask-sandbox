"""The routes module."""

from intro_to_flask import app
from flask import render_template, request, flash
from flask.ext.mail import Message, Mail

from forms import ContactForm


mail = Mail()


@app.route('/')
def home():
    """A simple home view."""
    return render_template('home.html')


@app.route('/about')
def about():
    """A simple about view."""
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['angeloski@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)
