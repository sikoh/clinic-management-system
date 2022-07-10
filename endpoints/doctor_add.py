from db import *

from models.doctors import Doctors, doctor_schema

def doctor_add():
   form = request.form

   fields = ['first_name','last_name', 'specialty', 'email', 'password', 'sex', 'phone']
   req_fields = ['first_name','last_name', 'specialty', 'email', 'password']
   values = []
   
   for field in fields:
      form_value = form.get(field)
      if form_value in req_fields and form_value == " ":
         return jsonify (f'{field} is required field'), 400

      values.append(form_value)
   
   first_name = form.get('first_name')
   last_name = form.get('last_name')
   specialty = form.get('specialty')
   email = form.get('email')
   password = form.get('password')
   sex = form.get('sex')
   phone = form.get('phone')


   new_doctor_record = Doctors(first_name, last_name, specialty, email, password, sex, phone)

   db.session.add(new_doctor_record)
   db.session.commit()
   
   return jsonify('Doctor Added', doctor_schema.dump(new_doctor_record)), 200