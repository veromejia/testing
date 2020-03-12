#!/usr/bin/python3

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.db_storage import DBStorage
from backend.models.prescription import Prescription
from backend.models.patient import Patient


from datetime import datetime
from twilio.rest import Client
from pathlib import Path

import os

account_sid = "MyTwillioAcc"
auth_token = "MyTwillioToken"
client = Client(account_sid, auth_token)

db = DBStorage()

date = datetime.strptime('{} {}'.format(sys.argv[2],sys.argv[3]), '%Y-%m-%d %H:%M:%S')
path = '{}/TaskManager'.format(str(Path.home()))
myfile = open('{}/job.txt'.format(path),'a+')
for prescription in db.all_prescription():
    if prescription.start_dt == date and prescription.frequency == sys.argv[1] and prescription.end_dt > date and prescription.noti_type == 'phone':
        patient = db.all_patients_by_id(prescription.patient_id)
        message = "Sending message to the patient: {} prescription: {} Access Date: {}\n".format(patient.id,prescription.medication,datetime.now())
        myfile.write(message)
        client.messages.create(
            to = patient.phone,
            from_ = "myTwilioPhone",
            body = prescription.medication
        )
        message = "Message successfully sent to the patient: {} acces date:\n".format(patient.id,datetime.now())
        myfile.write(message)
myfile.close()
"""
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
"""