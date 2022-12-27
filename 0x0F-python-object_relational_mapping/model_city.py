#!/usr/bin/python3
"""
A City class to work with SQLAlchemy ORM.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
        
        Attributes:
            __tablename__ (str): The table name of the class
            id (int): The State id of the class
            name (str): The State name of the class
            state_id (int): The state the cit belongs to
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
