from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import marshmallow as ma


from models.visits import Visits
from db import *


class Bills(db.Model):
    __tablename__ = "bills"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    visit_id = db.Column(UUID(as_uuid=True), db.ForeignKey('visits.id', ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    status = db.Column(db.String(), nullable = False)
    

    def __init__(self, visit_id, created_at, updated_at, status):
        self.visit_id = visit_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status

class BillsSchema(ma.Schema):
    class Meta:
        fields = ['id','visit_id', 'created_at', 'updated_at', 'status']

bill_schema = BillsSchema()
bills_schema = BillsSchema(many=True)