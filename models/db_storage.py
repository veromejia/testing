#!/usr/bin/python3
"""DataBase Storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from patient import Patient
import json


class DBStorage:
    """class for DBStorage"""
    __engine = None
    __session = None

    def __init__(self):

        """Constructor DBStorage"""
        with open('db_properties.json') as file:
            data = json.load(file)

            for prop in data['props']:
                user = prop['USER']
                pwd = prop['PWD']
                host = prop['HOST']
                database = prop['DB']
                #print('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, database))
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, database))
        print(self.__engine)
        

    def all_patients(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        for patient in self.__session.query(Patient).order_by(Patient.id).all():
            print("{}: {}".format(patient.id, patient.name))
        self.__session.close()

