#!/usr/bin/python

# encoding=utf-8
from flask.ext.script import Manager
from app.view import app
manager = Manager(app)
app.config['DEBUG'] = True
if __name__ == '__main__':
    manager.run()
