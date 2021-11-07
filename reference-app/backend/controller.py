# Built-in packages

# Third-party packages
from flask import Flask, request, jsonify

# Local packages
from database import db


def register_controllers(app: Flask) -> None:
    @app.route("/")
    def homepage():
        return jsonify({"message": "Hello World!"})

    @app.route("/api")
    def api():
        answer = "something"
        return jsonify(repsonse=answer)

    @app.route("/star", methods=["POST"])
    def add_star():
        star = db.stars
        name = request.json["name"]
        distance = request.json["distance"]
        star_id = star.insert({"name": name, "distance": distance})
        new_star = star.find_one({"_id": star_id})
        output = {"name": new_star["name"], "distance": new_star["distance"]}
        return jsonify({"result": output})
