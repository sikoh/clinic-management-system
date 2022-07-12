from db import *

from models.doctors import Doctors, doctor_schema

def doctor_deactivate(doctor_id):
  doctor_record = db.session.query(Doctors).filter(Doctors.id == doctor_id).first()
  if not doctor_record:
    return ('Doctor not found'), 404
    
  doctor_record.active = False
  db.session.commit()

  return jsonify("User deactivated", doctor_schema.dump(doctor_record)), 201