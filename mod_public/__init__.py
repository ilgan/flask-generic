from flask.blueprints import Blueprint
import db
from flask import Blueprint, jsonify, redirect, url_for, render_template


mod_public = Blueprint("public", __name__, url_prefix="/public")


# @app.before_first_request
# def create_tables():
#     db.create_all()


# @app.errorhandler(ValidationError)
# def handle_marshmallow_validation(err):
#     return jsonify(err.messages), 400

@mod_public.route("/index", methods=["GET"])
def index():
    print("in public")
    result = "My Result"
    return render_template("mod_public/index.html", result=result), 200
