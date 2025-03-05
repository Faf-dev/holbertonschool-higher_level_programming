#!/usr/bin/python3
"""
Create a class definition of a state and an instance
base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class : Inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,)
    name = Column(String(128), nullable=False)
