from db import *
from models.visits import Visits, visits_schema

def visit_search(search_term):
   visit_results = []
   if search_term:
      search_term = search_term.lower()

      ''' SELECT * FROM visits 
                   WHERE id LIKE '%search_term%' 
                   OR doctor_id LIKE '%search_term%' 
                   OR patient_id LIKE '%search_term%' 
                   OR complaints LIKE '%search_term%' 
                   OR findings LIKE '%search_term%' 
                   OR date LIKE '%search_term%' 
                   OR created_at LIKE '%search_term%' 
                   OR updated_at LIKE '%search_term%' 
      '''

      visit_results = db.session.query(Visits) \
         .filter(db.or_( \
            db.func(Visits.id).contains(search_term), \
            db.func(Visits.doctor_id).contains(search_term), \
            db.func(Visits.patient_id).contains(search_term), \
            db.func.lower(Visits.complaints).contains(search_term), \
            db.func.lower(Visits.findings).contains(search_term), \
            db.func(Visits.date).contains(search_term), \
            db.func(Visits.created_at).contains(search_term), \
            db.func(Visits.updated_at).contains(search_term))) \
         .all()
      print(visit_results)     
   else:
      return jsonify('No search term sent'), 400
  #  return (visit_results)
   return jsonify(visits_schema.dump(visit_results)), 200