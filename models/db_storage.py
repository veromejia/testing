#!/usr/bin/python3
"""DataBase Storage"""
from prescription import Prescription
from patient import Base, Patient
from task_x_prescription import Task_x_prescription
from task import Task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        with open('db_properties.json') as file:
            data = json.load(file)

            for prop in data['props']:
                user = prop['USER']
                pwd = prop['PWD']
                host = prop['HOST']
                database = prop['DB']
                print('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, database))
                print ("")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, database), pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
    
    def all_patients(self):
        #Session = sessionmaker(bind=self.__engine)
        #self.__session = Session()
        for patient in self.__session.query(Patient).order_by(Patient.id).all():
            print("{}: {}".format(patient.id, patient.name))
        self.__session.close()
        print("")

    def all_prescription(self):
        #Session = sessionmaker(bind=self.__engine)
        #self.__session = Session()
        for prescription in self.__session.query(Prescription).order_by(Prescription.id).all():
            print("{}: {}".format(prescription.id, prescription.medication))
        self.__session.close()
   
    def all_task(self):
        #Session = sessionmaker(bind=self.__engine)
        #self.__session = Session()
        for task in self.__session.query(Task).order_by(Task.id).all():
            print("{}: {}".format(task.id,task.status))
        self.__session.close()

    def all_task_x_prescription(self):
        #Session = sessionmaker(bind=self.__engine)
        #self.__session = Session()
        for task_x_prescription in self.__session.query(Task_x_prescription).all():
            print("{}: {}".format(task_x_prescription.task_id, task_x_prescription.prescription_id))
        self.__session.close()    

x = DBStorage().all_patients()
y = DBStorage().all_prescription()
z = DBStorage().all_task_x_prescription()
zz = DBStorage().all_task()