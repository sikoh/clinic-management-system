# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import or_
import uuid
from datetime import datetime
import marshmallow as ma

from db import *

# app = Flask(__name__)

# database_host = "127.0.0.1:5432"
# database_name = "clinic"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# ma = Marshmallow(app)


class Medications(db.Model):
    __tablename__ = "medications"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    code = db.Column(db.String(), nullable = False)
    name = db.Column(db.String(), nullable = False)
    classification = db.Column(db.String(), nullable = False)
    
    prescription = db.relationship('Prescriptions', cascade="all,delete", backref = 'medications', lazy=True)
  
    

    def __init__(self, code, name, classification):
        self.code = code
        self.name = name
        self.classification = classification

class MedicationsSchema(ma.Schema):
    class Meta:
        fields = ['id','code', 'name', 'classification']

medication_schema = MedicationsSchema()
medications_schema = MedicationsSchema(many=True)