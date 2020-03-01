#!/usr/bin/python3
"""Class Patient"""
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Notificaction(Base):
    __tablename__ = 'notification'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Auto-increment should be default
    prescription_id = Column(Integer, ForeignKey(
        'prescription.id'), nullable=False)
    start_dt = Column(DateTime, nullable=False, default=DateTime.utcnow())
    end_dt = Column(DateTime, nullable=False, default=DateTime.utcnow())
    last_dt = Column(DateTime, default=DateTime.utcnow())
    noti_type = Column(String(60))
    tasks = relationship(
        'Task', backref='notification', cascade='all, delete-orphan')
