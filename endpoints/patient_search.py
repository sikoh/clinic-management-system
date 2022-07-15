from db import *
from models.patients import Patients, patients_schema

def patient_search(search_term):
   patient_results = []
   if search_term:
      search_term = search_term.lower()

      ''' SELECT * FROM patients 
                   WHERE first_name LIKE '%search_term%' 
                   OR last_name LIKE '%search_term%' 
                   OR email LIKE '%search_term%' 
                   OR phone LIKE '%search_term%' 
      '''

      patient_results = db.session.query(Patients) \
         .filter(db.or_( \
            db.func.lower(Patients.first_name).contains(search_term), \
            db.func.lower(Patients.last_name).contains(search_term), \
            db.func.lower(Patients.email).contains(search_term), \
            db.func.lower(Patients.phone).contains(search_term))) \
         .all()
   else:
      return jsonify('No search term sent'), 400
   return jsonify(patients_schema.dump(patient_results)), 200