import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250),nullable= False)
    password = Column(String(250),nullable=False)
    favorites=relationship('Favourite')

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    characters=relationship('Character')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship('User')
    character = relationship('Character')
    planet = relationship('Planet')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
