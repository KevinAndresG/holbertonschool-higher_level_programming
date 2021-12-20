#!/usr/bin/python3
"""
    conect with the database
    and create a new table
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)


class State (Base):
    """
        Create the new
        Table named states
    """
    __tablename__ = "states"
    id = Column(Integer(), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    Session = sessionmaker(bind=engine)
    session = Session()
