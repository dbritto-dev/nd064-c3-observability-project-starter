# Built-in packages

# Third-party packages
from flask import Flask

# Local packages


def create_app() -> Flask:
    app = Flask(__name__)

    from telemetry import register_telemetry
    from controller import register_controllers

    register_telemetry(app)
    register_controllers(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=8080)
