#!/usr/bin/python3
from backend.models.db_storage import DBStorage
from backend.models.patient import Patient
from backend.models.prescription import Prescription
from backend.models.task import Task
from backend.models.task_x_prescription import Task_x_prescription
from datetime import datetime
from crontab import CronTab 
import os 

class TaskManager:

    def findMyTask(self, frequency,startDt):
        db = DBStorage()
        task = db.task_by_command('python3 job.py {} {}'.format(frequency,startDt))
        return task
    
    def prescriptionsWithoutTasks(self):
        db = DBStorage()
        patients = db.all_patients()
        task = []
        
        for patient in patients:
            if not patient.prescriptions:
                print('No hay prescipciones para el paciente {}'.format(patient.name))
            else:
                for prescription in patient.prescriptions:
                    print(prescription.id)
                    if not prescription.task_x_prescriptions:
                        print('The prescription {} does not have a task , sitting taskConfiguration'.format(prescription.medication))
                        task = self.findMyTask(prescription.frequency,prescription.start_dt)
                        if not task:
                            print('No task matching with the frequency {} and the start date {} proceding to create the task'.format(prescription.frequency,prescription.start_dt))
                            t = Task(task_command='python3 job.py {} {}'.format(prescription.frequency,prescription.start_dt),task_comment='medr-{}'.format(prescription.id),last_dt=datetime.now(),status='NEW0')
                            db.add_task(t)
                            print('Task created succesfully')
                            db.add_task_x_prescription( Task_x_prescription(task_id = t.id,prescription_id = prescription.id) )
                            print('The relation with the prescription {} was created for the task {}'.format(prescription.id,t.id))
                        else:
                            #print('task id {}'.format(task[0].id))
                            t = task[0]
                            print('One  task match with the frequency {} and the start date {} proceding to set the configuration'.format(prescription.frequency,prescription.start_dt))
                            db.add_task_x_prescription( Task_x_prescription(task_id = t.id,prescription_id = prescription.id) )
                            print('The relation between task and prescription was established')
    def createCron(self):
        #session.query(Task)
        message = "1"
        crons = 0
        db = DBStorage()
        cron = CronTab()
        os_user = 'nelson'

        for task in db.all_new_tasks():
            args = task.task_command.split()
            date = datetime.strptime('{} {}'.format(args[3],args[4]), '%Y-%m-%d %H:%M:%S')
            if  date <= datetime.now():
                path = os.getcwd()
                cron = CronTab(user=os_user)
                job = cron.new(command='{}/{}'.format(path,task.task_command),comment="medr-{}".format(task.id))
                job.hour.every(int(args[2]))
                cron.write()
                task.status_cd = "CRTD"
                db.get_session().commit()
    
        print("The following cron's were created: ".format(crons))
        for item in cron:
            print(item)
   
        db.get_session().close()

                            
tm = TaskManager()
tm.prescriptionsWithoutTasks()
tm.createCron()