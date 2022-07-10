from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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


class Prescriptions(db.Model):
    __tablename__ = "prescriptions"
    # id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    medication_id = db.Column(UUID(as_uuid=True), db.ForeignKey('medications.id', ondelete="CASCADE"), primary_key=True, nullable=False)
    visit_id = db.Column(UUID(as_uuid=True), db.ForeignKey('visits.id', ondelete="CASCADE"), primary_key=True, nullable=False)
    

    def __init__(self, medication_id, visit_id):
        self.medication_id = medication_id
        self.visit_id = visit_id


class PrescriptionsSchema(ma.Schema):
    class Meta:
        fields = ['procedure_id','visit_id']

prescription_schema = PrescriptionsSchema()
prescriptions_schema = PrescriptionsSchema(many=True)