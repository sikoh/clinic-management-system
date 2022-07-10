from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma
import uuid
from datetime import datetime
import endpoints


app = Flask(__name__)
database_host = "127.0.0.1:5432"
database_name = "clinic"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()
ma = Marshmallow(app)


from models.bills import Bills
from models.doctors import Doctors
from models.medications import Medications
from models.patients import Patients
from models.prescriptions import Prescriptions
from models.procedures import Procedures
from models.visit_procedures import VisitProcedures
from models.visits import Visits

# from db import *



def create_all():
   with app.app_context():
      db.create_all()

      print("Querying for Super Admin user...")
      doctor_data = db.session.query(Doctors).filter(Doctors.email == 'clinic-admin@testemail.com').first()
      if doctor_data == None:
         print("Super Admin not found! Creating clinic-admin@testemail user...")
         password = ''
         while password == '' or password is None:
            password = input(' Enter a password for Super Admin:')

         record = Doctors('Super', 'Admin', 'admin', 'clinic-admin@testemail.com', password,'U', 1231231234,1)


         db.session.add(record)
         db.session.commit()
      else:
         print("Super Admin user found!")




@app.route('/doctor/add', methods=['POST'])
def doctor_add():
    return endpoints.doctor_add()








if __name__ == "__main__":
    create_all()
    app.run(debug=True)