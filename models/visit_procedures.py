from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import *


class VisitProcedures(db.Model):
    __tablename__ = "visit_procedures"
    procedure_id = db.Column(UUID(as_uuid=True), db.ForeignKey('procedures.id', ondelete="CASCADE"), primary_key=True, nullable=False)
    visit_id = db.Column(UUID(as_uuid=True), db.ForeignKey('visits.id', ondelete="CASCADE"), primary_key=True, nullable=False)
    

    

    def __init__(self, procedure_id, visit_id):
        self.procedure_id = procedure_id
        self.visit_id = visit_id


class VisitProceduresSchema(ma.Schema):
    class Meta:
        fields = ['procedure_id','visit_id']

visit_procedure_schema = VisitProceduresSchema()
visit_procedures_schema = VisitProceduresSchema(many=True)