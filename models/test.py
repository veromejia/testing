from patient import Patient
from sqlalchemy.orm import sessionmaker

db = DBStorage()

Session = sessionmaker(bind=db.__engine)
db.__session = Session()

for patient in db._session.query(Patient).order_by(Patient.id).all():
    print("{}: {}".format(patient.id, patient.name))
db.__session.close()