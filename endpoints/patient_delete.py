from db import *

from models.patients import Patients

def patient_delete(patient_id):
  patient_record = db.session.query(Patients).filter(Patients.id == patient_id).first()

  if patient_record:
      db.session.delete(patient_record)
      db.session.commit()
      return jsonify(f'Patient with patient_id {patient_id} is deleted'), 200


  return (f'Patient with patient_id {patient_id} not found'), 404