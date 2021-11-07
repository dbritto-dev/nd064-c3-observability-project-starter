# Built-in packages

# Third-party packages
from flask import Flask, render_template

# Local packages


def register_controllers(app: Flask) -> None:
    @app.route("/")
    def homepage():
        return render_template("main.html")
