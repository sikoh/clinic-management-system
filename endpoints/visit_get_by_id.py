from db import *

from models.visits import Visits, visit_schema


def visit_get_by_id(visit_id):

   visit_record = db.session.query(Visits).filter(Visits.id == visit_id).first()
   
   if visit_record:
        return jsonify(visit_schema.dump(visit_record))

   return jsonify(f'Visit with vist_id {visit_id} not found'), 404