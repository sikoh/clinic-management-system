# from email.policy import default
# from flask import request, Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import or_
import uuid
import marshmallow as ma


from db import *
# app = Flask(__name__)

# database_host = "127.0.0.1:5432"
# database_name = "clinic"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# ma = Marshmallow(app)


class Doctors(db.Model):
    __tablename__ = "doctors"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String(), nullable = False)
    last_name = db.Column(db.String(), nullable = False)
    specialty= db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False, unique=True)
    password = db.Column(db.String(), nullable = False)
    sex = db.Column(db.String())
    phone = db.Column(db.String())
    active = db.Column(db.Boolean(), nullable = False, default = True)
    
    visit = db.relationship('Visits', cascade="all,delete", backref = 'doctors', lazy=True)



    def __init__(self, first_name,last_name, specialty, email, password, sex, phone, active = True):
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.email = email
        self.password = password
        self.sex = sex
        self.phone = phone
        self.ative = active

class DoctorsSchema(ma.Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'specialty', 'email']

doctor_schema = DoctorsSchema()
doctors_schema = DoctorsSchema(many=True)