from db import *

from models.patients import Patients, patients_schema

def patient_list():
   patients_records = db.session.query(Patients).all()

   return jsonify(patients_schema.dump(patients_records)), 200