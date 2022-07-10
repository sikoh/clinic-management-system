from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID

from models.bills import Bill
from models.doctors import Doctor
from models.medications import Medication
from models.patients import Patient
from models.prescriptions import Prescription
from models.procedures import Procedure
from models.visit_procedures import VisitProcedure
from models.visits import Visit

from db import *

app = Flask(__name__)

database_host = "127.0.0.1:5432"
database_name = "clinic"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)


def create_all():
   print("Querying for Super Admin user...")
   user_data = db.session.query(Doctor).filter(Doctor.email == 'clinic-admin@testemail.com').first()
   if user_data == None:
      print("Super Admin not found! Creating clinic-admin@testemail user...")
      password = ''
      while password == '' or password is None:
         password = input(' Enter a password for Super Admin:')

      record = Doctor('Super', 'Admin', 'admin', "admin@devpipeline.com", password)

      db.session.add(record)
      db.session.commit()
   else:
      print("Super Admin user found!")
    