# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import or_
import uuid
from datetime import datetime
import marshmallow as ma


from models.visits import Visits
from db import *

# app = Flask(__name__)
# db = SQLAlchemy(app)

# # database_host = "127.0.0.1:5432"
# # database_name = "clinic"
# # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# ma = Marshmallow(app)



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
        fields = ['id','first_name', 'last-name', 'sex', 'phone', 'dob', 'active']

bill_schema = BillsSchema()
bills_schema = BillsSchema(many=True)