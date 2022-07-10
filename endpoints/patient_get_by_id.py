from db import *
from models.patients import Patients, patient_schema


def patient_get_by_id(patient_id):

   patient_record = db.session.query(Patients).filter(Patients.id == patient_id).first()
   
   if patient_record:
        return jsonify(patient_schema.dump(patient_record))

   return jsonify(f'User with doctor_id {patient_id} not found'), 404