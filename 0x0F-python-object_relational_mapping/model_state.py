#!/usr/bin/python3
"""
    conect with the database
    and create a new table
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State (Base):
    """
        Create the new
        Table named states
    """
    __tablename__ = "states"
    id = Column(Integer(), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
