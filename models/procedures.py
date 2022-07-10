from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma

from db import *

class Procedures(db.Model):
    __tablename__ = "procedures"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    code = db.Column(db.String(), nullable = False)
    name = db.Column(db.String(), nullable = False)
    cost = db.Column(db.Float(), nullable = False)
    
    visit_procedure = db.relationship('VisitProcedures', cascade="all,delete", backref = 'procedures', lazy=True)
    

    def __init__(self, code, name, cost):
        self.code = code
        self.name = name
        self.cost = cost

class ProceduresSchema(ma.Schema):
    class Meta:
        fields = ['id','code', 'name', 'cost']

procedure_schema = ProceduresSchema()
procedures_schema = ProceduresSchema(many=True)