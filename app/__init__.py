from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/localDbase"  # Update this URI to your MongoDB instance

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localDbase.db'  # Update this URI for your preferred SQL database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

mongo = PyMongo(app)

from app import routes
