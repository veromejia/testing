#!/usr/bin/python3
"""Class Patient"""
from prescription import Prescription
from patient import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime


class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    prescription_id = Column(Integer, ForeignKey(
        'prescription.id'), nullable=False)
    start_dt = Column(DateTime, nullable=False, default=datetime.utcnow())
    end_dt = Column(DateTime, nullable=False, default=datetime.utcnow())
    last_dt = Column(DateTime, default=datetime.utcnow())
    noti_type = Column(String(60))
    tasks = relationship('Task',backref='notifications')#, backref='notification', cascade='all, delete-orphan')
