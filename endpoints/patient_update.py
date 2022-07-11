from db import *

from models.patients import Patients, patient_schema

def patient_update(patient_id):
  patient_record = db.session.query(Patients).filter(Patients.id == patient_id).first()

  if not patient_record:
    return (f'Patient with patient_id {patient_id} not found'), 404
  if request:
    form = request.form
    first_name = form.get('first_name')
    last_name = form.get('last_name')
    specialty = form.get('specialty')
    email = form.get('email')
    password = form.get('password')
    sex = form.get('sex')
    phone = form.get('phone')
    active = form.get('active')

  if first_name:
    patient_record.first_name = first_name
  if last_name:
    patient_record.last_name = last_name
  if specialty:
    patient_record.specialty = specialty
  if email:
    patient_record.email = email
  if password:
    patient_record.password = password
  if sex:
    patient_record.sex = sex
  if phone:
    patient_record.phone = phone
  if active:
    patient_record.active = active

  db.session.commit()

  return jsonify('Patient Updated', patient_schema.dump(patient_record)), 201