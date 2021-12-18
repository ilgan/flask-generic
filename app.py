from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from dotenv import load_dotenv

from db import db
from ma import ma
from resources.user import User

app = Flask(__name__)
load_dotenv(".env")
app.config.from_object("config.py")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


api.add_resource(User, "/user/<int:user_id>")
