from db import *
from models.doctors import Doctors, doctor_schema


def doctor_get_by_id(doctor_id):

   doctor_record = db.session.query(Doctors).filter(Doctors.id == doctor_id).first()
   
   if doctor_record:
        return jsonify(doctor_schema.dump(doctor_record))

   return jsonify(f'Doctor with doctor_id {doctor_id} not found'), 404