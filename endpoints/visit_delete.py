from db import *

from models.visits import Visits

def visit_delete(visit_id):
  visit_record = db.session.query(Visits).filter(Visits.id == visit_id).first()

  if visit_record:
      db.session.delete(visit_record)
      db.session.commit()
      return jsonify(f'Visit with visit_id {visit_id} is deleted'), 200
      
  return (f'Visit with visit_id {visit_id} not found'), 404