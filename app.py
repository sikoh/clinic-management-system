from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
# import marshmallow as ma
import uuid
from datetime import datetime
import endpoints


app = Flask(__name__)
database_host = "127.0.0.1:5432"
database_name = "clinic"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()
ma = Marshmallow(app)


from models.doctors import Doctors


def create_all():
   with app.app_context():
      db.create_all()

      print("Querying for Super Admin user...")
      doctor_data = db.session.query(Doctors).filter(Doctors.email == 'clinic-admin@testemail.com').first()
      if doctor_data == None:
         print("Super Admin not found! Creating clinic-admin@testemail user...")
         password = ''
         while password == '' or password is None:
            password = input(' Enter a password for Super Admin:')

         record = Doctors('Super', 'Admin', 'admin', 'clinic-admin@testemail.com', password,'U', 1231231234, 1)


         db.session.add(record)
         db.session.commit()
      else:
         print("Super Admin user found!")




@app.route('/doctor/add', methods=['POST'])
def doctor_add():
    return endpoints.doctor_add()

@app.route('/doctor/list', methods=['GET'])
def doctor_list():
    return endpoints.doctor_list()

@app.route("/doctor/<doctor_id>", methods=["GET"])
def doctor_get_by_id(doctor_id):
    return endpoints.doctor_get_by_id(doctor_id)

@app.route("/doctor/update/<doctor_id>", methods=["POST"])
def doctor_update(doctor_id):
    return endpoints.doctor_update(doctor_id)

@app.route("/doctor/delete/<doctor_id>", methods=["DELETE"])
def doctor_delete(doctor_id):
    return endpoints.doctor_delete(doctor_id)

@app.route("/doctor/activate/<doctor_id>", methods=["PUT"])
def doctor_activate(doctor_id):
    return endpoints.doctor_activate(doctor_id)

@app.route("/doctor/deactivate/<doctor_id>", methods=["PUT"])
def doctor_deactivate(doctor_id):
    return endpoints.doctor_deactivate(doctor_id)

@app.route("/doctor/search/<search_term>", methods=["GET"])
def get_records_by_search(search_term):
    return endpoints.doctor_search(search_term)



@app.route('/patient/add', methods=['POST'])
def patient_add():
    return endpoints.patient_add()

@app.route('/patient/list', methods=['GET'])
def patient_list():
    return endpoints.patient_list()

@app.route("/patient/<patient_id>", methods=["GET"])
def patient_get_by_id(patient_id):
    return endpoints.patient_get_by_id(patient_id)

@app.route("/patient/update/<patient_id>", methods=["POST"])
def patient_update(patient_id):
    return endpoints.patient_update(patient_id)

@app.route("/patient/delete/<patient_id>", methods=["DELETE"])
def patient_delete(patient_id):
    return endpoints.patient_delete(patient_id)

@app.route("/patient/search/<search_term>", methods=["GET"])
def patients_search(search_term):
    return endpoints.patient_search(search_term)




@app.route('/visit/add', methods=['POST'])
def visit_add():
    return endpoints.visit_add()

@app.route('/visit/list', methods=['GET'])
def visit_list():
    return endpoints.visit_list()

@app.route("/visit/<visit_id>", methods=["GET"])
def visit_get_by_id(visit_id):
    return endpoints.visit_get_by_id(visit_id)

@app.route("/visit/delete/<visit_id>", methods=["DELETE"])
def visit_delete(visit_id):
    return endpoints.visit_delete(visit_id)

@app.route("/visit/search/<search_term>", methods=["GET"])
def visit_search(search_term):
    return endpoints.visit_search(search_term)



if __name__ == "__main__":
    create_all()
    app.run(debug=True)