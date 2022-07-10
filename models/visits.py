from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import or_
import uuid
from datetime import datetime
import marshmallow as ma

app = Flask(__name__)

# database_host = "127.0.0.1:5432"
# database_name = "clinic"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Visit(db.Model):
    __tablename__ = "visits"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    doctor_id = db.Column(UUID(as_uuid=True), db.ForeignKey('doctors.id', ondelete="CASCADE"), nullable=False)
    patient_id = db.Column(UUID(as_uuid=True), db.ForeignKey('patients.id', ondelete="CASCADE"), nullable=False)
    date = db.Column(db.DateTime(), nullable = False)
    status = db.Column(db.String(), nullable = False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    bill = db.relationship('Bill', cascade="all,delete", backref = 'visit', lazy=True)
    prescription = db.relationship('Prescription', cascade="all,delete", backref = 'visit', lazy=True)
    visit_procedure = db.relationship('VisitProcedure', cascade="all,delete", backref = 'visit', lazy=True)
    
    

    def __init__(self, doctor_id, patient_id, date, status, created_at, updated_at):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        

class BillSchema(ma.Schema):
    class Meta:
        fields = ['id','first_name', 'last-name', 'sex', 'phone', 'dob', 'active']

bill_schema = BillSchema()
bills_schema = BillSchema(many=True)