from db import *

from models.visits import Visits, visits_schema

def visit_list():
   visits_records = db.session.query(Visits).all()

   return jsonify(visits_schema.dump(visits_records)), 200