# from flask import request, Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import or_
import uuid
from datetime import datetime
import marshmallow as ma

# app = Flask(__name__)

# database_host = "127.0.0.1:5432"
# database_name = "clinic"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# ma = Marshmallow(app)
from db import db 

class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String(), nullable = False)
    last_name = db.Column(db.String(), nullable = False)
    sex = db.Column(db.String(), nullable = False)
    phone = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False, unique=True)
    password = db.Column(db.String(), nullable = False)
    dob = db.Column(db.DateTime(), nullable = False)
    visit = db.relationship('Visit', cascade="all,delete", backref = 'patient', lazy=True)

    def __init__(self, first_name,last_name, sex, phone, email, password, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.phone = phone
        self.email = email
        self.password = password
        self.dob = dob

class PatientSchema(ma.Schema):
    class Meta:
        fields = ['id','first_name', 'last-name', 'sex', 'phone', 'dob', 'active']

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)