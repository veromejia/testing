#!/usr/bin/python3

import sys
#from TaskModel import Base,Task
from task import Base,Task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from crontab import CronTab 

host = 'localhost'
user = 'user_medreminder'
pas = 'pwd_medreminder'
db = 'db_medreminder'
uri = ''
cron = CronTab()

#if __name__ == '__main__':
 #   uri='mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],sys.argv[3])
#else:
uri='mysql+mysqldb://{}:{}@localhost/{}'.format(user, pas,db)

engine = create_engine(uri, pool_pre_ping=True)
#Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
    
session = Session()

#session.query(Task)
message = "1"
crons = 0
for task in session.query(Task).filter(Task.status == "NEW0").all():
        message = "{}:  Access Date {}\n".format(task.name,datetime.now())
        myfile = open('/home/nelson/Documents/medreminder_app/testPython/job.txt','a+')
        myfile.write(message)
        myfile.close()
        
        """Proceding to create a new cron job to fire the alert"""
        cron = CronTab(user='nelson')
        job = cron.new(command='python3 /home/nelson/Documents/medreminder_app/testPython/job.py',comment="medr-{}".format(task.id))
        job.minute.every(int(task.frequency))
        cron.write()
        task.status_cd = "CRTD"
        session.commit()
        crons = crons + 1

print("The following cron's were created: ".format(crons))
for item in cron:
    print(item)
   

session.close()

#TO see cron's created by the user nelson 
#crontab -u nelson -l