from db import *

from models.patients import Patients, patient_schema

def patient_add():
   form = request.form

   fields = ['first_name','last_name', 'sex', 'phone', 'email', 'dob']

   values = []
   
   for field in fields:
      form_value = form.get(field)
      if form_value == "" or form_value == None:
         return jsonify (f'{field} is required field'), 400

      values.append(form_value)
   

   first_name = form.get('first_name')
   last_name = form.get('last_name')
   sex = form.get('sex')
   phone = form.get('phone')
   email = form.get('email')
   dob = form.get('dob')
   
  


   new_patient_record = Patients(first_name, last_name, sex, phone, email, dob)

   db.session.add(new_patient_record)
   db.session.commit()
   
   return jsonify('Patient Added', patient_schema.dump(new_patient_record)), 200