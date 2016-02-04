"""Where all the forms live."""

from flask.ext.wtf import Form
from wtforms.fields import SubmitField, TextAreaField, TextField
from wtforms.validators import Required, Email


class ContactForm(Form):
    """A form class."""

    name = TextField("Name", [Required("Please enter your name.")])
    email = TextField("Email", [Required("Please enter your email address."),
                                Email("Please enter your valid email address.")])
    subject = TextField("Subject", [Required("Please enter a subject.")])
    message = TextAreaField("Message", [Required("Please enter a message.")])
    submit = SubmitField("Send")
