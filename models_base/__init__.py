from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config')
base = PyMongo(app)

from . import views, forms
