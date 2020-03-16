from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, validators
from wtforms.fields.html5 import DateField
from datetime import datetime
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange,InputRequired
from backend.models.db_storage import DBStorage
from backend.models.patient import Patient
from backend.models.prescription import Prescription

class DashBoardForm(FlaskForm):
    patients = Patient()
    selectedid = ""
    
    
    def getPatients(self):
        db = DBStorage()
        self.patients = db.all_patients()
    
    def getPrescriptions(self):
        db = DBStorage()
        prescriptions = db.prescriptionXpatientID(int(self.selectedid))
        return prescriptions

    def getTasks(self,prescriptionID):
        tasks = []
        db = DBStorage()
        tasks = db.taskByPrescriptions(prescriptionID)
        return tasks

        

            
