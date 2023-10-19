from flask import Flask
from .todo import todo_dp


def register_blueprint(app: Flask):
    app.register_blueprint(todo_dp)
    # app.add_url_rule("/", endpoint="index")
    # add more blueprint
