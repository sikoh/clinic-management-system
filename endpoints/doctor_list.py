from db import *

from models.doctors import Doctors, doctors_schema

def doctor_list():
   doctor_records = db.session.query(Doctors).all()

   return jsonify(doctors_schema.dump(doctor_records)), 200