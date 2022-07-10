from sqlalchemy.dialects.postgresql import UUID

import uuid
from datetime import datetime
import marshmallow as ma

from db import *



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