# MedReminder
## Description
MedReminder is a web application that can send text message to patients who needed reminder to take their medication daily. User can enter the recipient's information and fill out a reminder page which allows the app to know what medication, the frequency and also the duration of this medication for each recipient.
## Inspiration
Veronica's mother has diabetes and she continously asked Veronica to send a text as a reminder to take her medication daily, but Veronica can not keep track of that since she is occupied with her busy schedule as well. This is when the idea of MedReminder emerged.
## Composition
### Tools

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/front-end.png" height="50%" width="50%"/>

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/back-end.png" />

### Architecture
<img src="https://github.com/veromejia/med_reminder/blob/master/Images/Architecture.png" />

## Requirements 📋
MedReminder is a Web Application designed to send a reminder whenever there is an active alert for that. The reminder can be:

1. A Text Message, which is sent through Twilio API. To run this project you will need to have a twilio trial account.
2. An email which is sent using a gmail account

_You should also install the following tools_

`$ sudo apt-get install python3-venv`

`$ pip install Flask`

`$ pip intall Jinja2`

`$ sudo apt-get install mysql-server`

`$ pip install SQLAlchemy`

`$ pip install python-crontab`

`$ pip install twilio`

### CONFIGURATION

_after installing the above mentioned requirements_

* Clone this repository https://github.com/veromejia/med_reminder.git
* copy the folder TaskManager that is inside of med_reminder folder to the home directory
* go to the python file Taskmanager/job.py that now is in your home directory and replace the values of the following varialbes `account_sid = "Mytwiliosid"`, `auth_token = "MytwilioToken"`, `from_="myTwilioPhoneNumber"`, `sender="myEmail@gmail.com"`, and `password ="​myEmailPassword"` with your own credentials. 

### TESTING

1- Run the Cron jobs
* go to the directory TaskManager that previously was copied in your home directory and run the python file setup.py 
`ex: ./setup.py
~/TaskManager$ ./setup.py 
The following cron's were created: 
* * * * * python3 /home/vero/TaskManager/taskmanager.py # medr-taskmanager`

This script will create the crons that will be run every minute to check if there are active tasks to send a reminder

note: to stop the crons that are runing every minut run the python file `CleanCrons.py`

2- Run the Web Application
* Go to the folder MedReminder and run the following command `env FLASK_APP = app.py flask `

### ex:
`~/med_reminder$ env FLASK_APP = app.py flask
Serving Flask app "app"
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

3- go to your favorite browser and type `localhost:5000` or `127.0.0.1:5000` to test this web application

## Demo Features
<img src="https://github.com/veromejia/med_reminder/blob/master/Images/landing%20page.png" />

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/About%20us.png" />

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/features.png" />

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/Demo%20page.png" />

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/Recipient%20info.png" />

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/Reminder%20info.png" />

<img src="https://github.com/veromejia/med_reminder/blob/master/Images/Dashboard%20record.png" />


## Authors
* Veronica Mejia [Github](https://github.com/veromejia)
* Hanh Nguyen [Github](https://github.com/hanhuyeny2k)