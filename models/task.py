#!/usr/bin/python3
"""Class Patient"""
from engine.db_storage import DBStorage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Auto-increment should be default
    notification_id = Column(
        Integer, ForeignKey('notifications.id'), nullable=False)
    name = Column(String(60))
    frecuency = Column(String(60), nullable=False)
    status = Column(String(60))
