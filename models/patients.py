from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma

from db import * 

class Patients(db.Model):
    __tablename__ = "patients"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String(), nullable = False)
    last_name = db.Column(db.String(), nullable = False)
    sex = db.Column(db.String(), nullable = False)
    phone = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False, unique=True)
    dob = db.Column(db.DateTime(), nullable = False)
    
    visit = db.relationship('Visits', cascade="all,delete", backref = 'patients', lazy=True)

    def __init__(self, first_name,last_name, sex, phone, email, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.phone = phone
        self.email = email
        self.dob = dob

class PatientsSchema(ma.Schema):
    class Meta:
        fields = ['id','first_name', 'last_name', 'sex', 'phone', 'email','dob']

patient_schema = PatientsSchema()
patients_schema = PatientsSchema(many=True)