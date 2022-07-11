from db import *

from models.doctors import Doctors

def doctor_delete(doctor_id):
  doctor_record = db.session.query(Doctors).filter(Doctors.id == doctor_id).first()

  if doctor_record:
      db.session.delete(doctor_record)
      db.session.commit()
      return jsonify(f'Doctor with doctor_id {doctor_id} is deleted'), 200
      
  return (f'Doctor with doctor_id {doctor_id} not found'), 404