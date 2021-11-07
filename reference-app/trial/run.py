# Built-in packages

# Third-party packages
from waitress import serve

# Local packages
from app import create_app


if __name__ == "__main__":
    serve(create_app(), server_name="trial-server", port=8080)
