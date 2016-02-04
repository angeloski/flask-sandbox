from intro_to_flask import app
from flask.ext.script import Manager

#app.run(debug=True)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
