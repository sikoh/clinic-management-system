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


class VisitProcedure(db.Model):
    __tablename__ = "visit_procedures"
    procedure_id = db.Column(UUID(as_uuid=True), db.ForeignKey('procedures.id', ondelete="CASCADE"), nullable=False)
    visit_id = db.Column(UUID(as_uuid=True), db.ForeignKey('visits.id', ondelete="CASCADE"), nullable=False)
    

    

    def __init__(self, procedure_id, visit_id):
        self.procedure_id = procedure_id
        self.visit_id = visit_id


class VisitProcedureSchema(ma.Schema):
    class Meta:
        fields = ['procedure_id','visit_id']

visit_procedure_schema = VisitProcedureSchema()
visit_procedures_schema = VisitProcedureSchema(many=True)