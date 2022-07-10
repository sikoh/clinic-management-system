from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import *



class Prescriptions(db.Model):
    __tablename__ = "prescriptions"
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