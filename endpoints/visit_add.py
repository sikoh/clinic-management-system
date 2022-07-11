from db import *
from datetime import datetime

from models.visits import Visits, visit_schema

def visit_add():
   form = request.form

   fields = ['doctor_id', 'patient_id', 'complaints','findings', 'date', 'status']
   values = []
   
   for field in fields:
      form_value = form.get(field)
      if form_value == " " or form_value == None:
         return jsonify (f'{field} is required field'), 400

      values.append(form_value)
   doctor_id = form.get ('doctor_id')
   patient_id = form.get ('patient_id')
   complaints = form.get('complaints')
   findings = form.get('findings')
   date = form.get('date')
   status = form.get('status')
   created_at = datetime.now()
   updated_at = datetime.now()
  


   new_visit_record = Visits(doctor_id, patient_id, complaints, findings, date, status, created_at, updated_at)

   db.session.add(new_visit_record)
   db.session.commit()
   
   return jsonify('New Visit is Added', visit_schema.dump(new_visit_record)), 200