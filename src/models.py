import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = "planets"

    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)

class FavPeople(Base):
    __tablename__ = "favpeople"
    id = Column(Integer, primary_key=True)
    User_ID = Column(Integer, ForeignKey('user.id'))
    People_ID = Column(Integer, ForeignKey('people.uid'))
    people = relationship(People)
    user = relationship(User)

class FavPlanets(Base):
    __tablename__ = "favplanets"
    id = Column(Integer, primary_key=True)
    User_ID = Column(Integer, ForeignKey('user.id'))
    Planet_ID = Column(Integer, ForeignKey('planets.uid'))
    planets = relationship(Planets)
    user = relationship(User)
    

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')