
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma
from db import db
from models.doctors import Doctors, DoctorsSchema, doctor_schema
from models.patients import Patients, PatientsSchema, patient_schema 


class Visits(db.Model):
    __tablename__ = "visits"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    doctor_id = db.Column(UUID(as_uuid=True), db.ForeignKey('doctors.id', ondelete="CASCADE"), nullable=False)
    patient_id = db.Column(UUID(as_uuid=True), db.ForeignKey('patients.id', ondelete="CASCADE"), nullable=False)
    complaints = db.Column(db.String(), nullable = False)
    findings = db.Column(db.String(), nullable = False)
    date = db.Column(db.DateTime(), nullable = False)
    status = db.Column(db.String(), nullable = False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    
    # bill = db.relationship('Bills', cascade="all,delete", backref = 'visits', lazy=True)
    # prescription = db.relationship('Prescriptions', cascade="all,delete", backref = 'visits', lazy=True)
    # visit_procedure = db.relationship('VisitProcedures', cascade="all,delete", backref = 'visits', lazy=True)
    # doctor = db.relationship('Doctors', cascade="all,delete", backref = 'visits', lazy=True)
    
    

    def __init__(self, doctor_id, patient_id, complaints, findings, date, status, created_at, updated_at):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.complaints = complaints
        self.findings = findings
        self.date = date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        

class VisitsSchema(ma.Schema):
    class Meta:
        # fields = ['id','doctor_id', 'patient_id', 'complains', 'findings', 'date', 'stutus', 'created_at', 'updated_at']
        fields = ['id','doctor', 'patient','complains', 'findings', 'date', 'status', 'created_at', 'updated_at']
        doctor = ma.fields.Nested(DoctorsSchema(only = ('first_name', 'last_name')))
        patient = ma.fields.Nested(PatientsSchema(only = ('first_name', 'last_name')))


visit_schema = VisitsSchema()
visits_schema = VisitsSchema(many=True)