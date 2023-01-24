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
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstName = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

    

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    name = Column(String(50), nullable=False)
    charactersID = Column(Integer)
    planetsID = Column(Integer)
    vehiclesID = Column(Integer)

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    # id = Column(Integer, primary_key=True)
    id = Column(Integer, ForeignKey('favorites.charactersID'), primary_key=True)
    favorites = relationship(Favorites)
    name = Column(String(50), nullable=False)
    img = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    detailsID = Column(String(50), nullable=False)

class CharacterDetails(Base):
    __tablename__ = 'character_details'
    id = Column(Integer, ForeignKey('characters.detailsID'), primary_key=True)
    characters = relationship(Characters)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    home_world = Column(String(250), nullable=False), ForeignKey('vehicles.url')
    films = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False), ForeignKey('vehicles.url')
    starship = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, ForeignKey('favorites.planetsID') , primary_key=True)
    favorites = relationship(Favorites)
    name = Column(String(50), nullable=False)
    img = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    detailsID = Column(String(50), nullable=False)

class PlanetsDetails(Base):
        __tablename__ = 'planets_details'
        id = Column(Integer, ForeignKey('planets.detailsID'), primary_key=True)
        planets = relationship(Planets)
        name = Column(String(250), nullable=False)
        climate = Column(String(250), nullable=False)
        created = Column(String(250), nullable=False)
        diameter = Column(String(250), nullable=False)
        edited = Column(String(250), nullable=False)
        films = Column(String(250), nullable=False)
        gravity = Column(String(250), nullable=False)
        orbital_period = Column(String(250), nullable=False)
        population = Column(String(250), nullable=False)
        residents = Column(String(250), nullable=False)
        rotation_period = Column(String(250), nullable=False)
        surface_water = Column(String(250), nullable=False)
        terrain = Column(String(250), nullable=False)
        url = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, ForeignKey('favorites.vehiclesID'), primary_key=True)
    favorites = relationship(Favorites)
    name = Column(String(50), nullable=False)
    img = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    detailsID = Column(String(50), nullable=False)

class VehiclesDetails(Base):
        __tablename__ = 'vehicles_details'
        id = Column(Integer, ForeignKey('vehicles.detailsID'), primary_key=True)
        vehicles = relationship(Vehicles)
        name = Column(String(250), nullable=False)
        cargo_capacity = Column(String(250), nullable=False)
        consumables = Column(String(250), nullable=False)
        cost_in_credits = Column(String(250), nullable=False)
        created = Column(String(250), nullable=False)
        crew = Column(String(250), nullable=False)
        edited = Column(String(250), nullable=False)
        length = Column(String(250), nullable=False)
        manofactured = Column(String(250), nullable=False)
        max_atmosphering_speed = Column(String(250), nullable=False)
        model = Column(String(250), nullable=False)
        passengers = Column(String(250), nullable=False)
        pilots = Column(String(250), nullable=False),ForeignKey('characters.url')
        films = Column(String(250), nullable=False)
        url = Column(String(250), nullable=False)
        vehicle_class = Column(String(250), nullable=False)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
