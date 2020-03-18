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
import smtplib, ssl
import os

account_sid = "mytwiliosid"
auth_token = "mytwiliotoken"
client = Client(account_sid, auth_token)

db = DBStorage()


def sendmail(email,prescription,frequency):
    port = 465
    sender = 'medreminderapp431@gmail.com'
    password = 'mypasswordemail'
    """print ('user:{} ,Pass: {}'.format(sender,password))"""
    recieve = email
    message = """
    Subject: medreminder
    
    Don't forget take your {} every {} hour
    
    Medreminder
    """.format(prescription,frequency)
    context = ssl.create_default_context()
   """print("Starting to send")"""
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    """print("sent email!")"""
            

date = datetime.strptime('{} {}'.format(sys.argv[2],sys.argv[3]), '%Y-%m-%d %H:%M:%S')
path = '{}/TaskManager'.format(str(Path.home()))
myfile = open('{}/job.txt'.format(path),'a+')
for prescription in db.all_prescription():
    if prescription.start_dt == date and prescription.frequency == sys.argv[1] and prescription.end_dt > datetime.now():
        patient = db.all_patients_by_id(prescription.patient_id)
        if prescription.noti_type == 'phone':
            """to have a register in the job.txt for everytime that is executed"""
            message = "Sending message to the patient: {} prescription: {} Access Date: {}\n".format(patient.id,prescription.medication,datetime.now())
            myfile.write(message)
            client.messages.create(
                to = patient.phone,
                from_ = "mytwiliophone",
                body = "Don't forget take your {} every {} hours".format(prescription.medication,prescription.frequency)
            )
            message = "Message successfully sent to the patient: {} acces date:\n".format(patient.id,datetime.now())
            myfile.write(message)
        else:
            message = "Sending email to the patient: {} prescription: {} Access Date: {}\n".format(patient.id,prescription.medication,datetime.now())
            myfile.write(message)
            sendmail(patient.email,prescription.medication,prescription.frequency)
            message = "Email successfully sent to the patient: {} acces date:\n".format(patient.id,datetime.now())
            myfile.write(message)
myfile.close()    

"""
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
"""