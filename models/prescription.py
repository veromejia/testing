#!/usr/bin/python3
"""Class Patient"""
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Prescription(Base):
    __tablename__ = 'prescription'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Auto-increment should be default
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    prescription = Column(String(120), nullable=False)
    notifications = relationship(
        'Notification', backref='prescription', cascade='all, delete-orphan')
