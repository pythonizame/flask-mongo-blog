# -*- coding: utf-8 -*-
__author__ = 'alex'
from flask.ext.script import Manager, Server
from blog import app


manager = Manager(app)


manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host="localhost",
))


if __name__ == "__main__":
    manager.run()
