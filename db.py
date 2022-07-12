
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
import uuid



app = Flask(__name__)



database_host = "127.0.0.1:5432"
database_name = "clinic"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
