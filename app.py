from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_session import Session
from marshmallow import ValidationError
# from dotenv import load_dotenv

from db import db
from ma import ma
from resources.user import User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app) #if decide to work with Restful instead of Blueprints
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, "/user/<int:user_id>")
