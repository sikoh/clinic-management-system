from db import *

from models.doctors import Doctors, doctor_schema

def doctor_activate(doctor_id):
  doctor_record = db.session.query(Doctors).filter(Doctors.id == doctor_id).first()
  if not doctor_record:
    return ('Doctor not found'), 404
    
  doctor_record.active = True
  db.session.commit()

  return jsonify("User Activated"), 201