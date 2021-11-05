# Built-in packages

# Third-party packages
from flask import Flask

# Local packages


def create_app() -> Flask:
    app = Flask(__name__)

    from tracing import register_instrumentors
    from controller import register_routes

    register_instrumentors(app)
    register_routes(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=8080)
