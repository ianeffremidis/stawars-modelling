import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250))
    gravity = Column(String(250))
    url = Column(String(250))
    
class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    homeworld = Column(String(250))
    url = Column(String(250))

class Starship(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    costInCredits = Column(String(250))
    url = Column(String(250))


class FavPlanets(Base):
    __tablename__ = 'favPlanets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, ForeignKey('user.id'))
    planetId = Column(Integer, ForeignKey('planet.id'))

class FavCharacters(Base):
    __tablename__ = 'favCharacters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, ForeignKey('user.id'))
    characterId = Column(Integer, ForeignKey('character.id'))

class FavStarships(Base):
    __tablename__ = 'favStarships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, ForeignKey('user.id'))
    starshipId =Column(Integer, ForeignKey('starship.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
