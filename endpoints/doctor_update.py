from db import *

from models.doctors import Doctors, doctor_schema

def doctor_update(doctor_id):
  doctor_record = db.session.query(Doctors).filter(Doctors.id == doctor_id).first()

  if not doctor_record:
    return (f'Doctor with doctor_id {doctor_id} not found'), 404
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
    doctor_record.first_name = first_name
  if last_name:
    doctor_record.last_name = last_name
  if specialty:
    doctor_record.specialty = specialty
  if email:
    doctor_record.email = email
  if password:
    doctor_record.password = password
  if sex:
    doctor_record.sex = sex
  if phone:
    doctor_record.phone = phone
  if active:
    doctor_record.active = active

  db.session.commit()

  return jsonify('Doctor Updated', doctor_schema.dump(doctor_record)), 201