# Built-in packages

# Third-party packages
from flask import Flask, jsonify

# Local packages


def register_controllers(app: Flask) -> None:
    @app.route("/")
    def homepage():
        return jsonify({"message": "Hello World!"})
