# Built-in packages

# Third-party packages
from flask import Flask
from flask_pymongo import PyMongo

# Local packages

mongo = PyMongo()
db = mongo.db


def register_db(app: Flask) -> None:
    app.config["MONGO_DBNAME"] = "example-mongodb"
    app.config[
        "MONGO_URI"
    ] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

    mongo.init_app(app)
