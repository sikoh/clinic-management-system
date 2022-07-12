from db import *
from models.doctors import Doctors, doctors_schema

def doctor_search(search_term):
   doctor_results = []
   if search_term:
      search_term = search_term.lower()

      ''' SELECT * FROM doctors 
                   WHERE first_name LIKE '%search_term%' 
                   OR last_name LIKE '%search_term%' 
                   OR specialty LIKE '%search_term%' 
                   OR email LIKE '%search_term%' 
                   OR phone LIKE '%search_term%' 
      '''

      doctor_results = db.session.query(Doctors) \
         .filter(db.or_( \
            db.func.lower(Doctors.first_name).contains(search_term), \
            db.func.lower(Doctors.last_name).contains(search_term), \
            db.func.lower(Doctors.specialty).contains(search_term), \
            db.func.lower(Doctors.email).contains(search_term), \
            db.func.lower(Doctors.phone).contains(search_term))) \
         .all()
   else:
      return jsonify('No search term sent'), 400
   return jsonify(doctors_schema.dump(doctor_results)), 200