#!/usr/bin/python3
"""This is the place class, okay"""
from models.base_model import BaseModel, Base
import models
from models.amenity import Amenity
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    place_amenity = Table('place_amenity',
                          Base.metadata,
                          Column('places_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenities_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )

    @property
    def amenities(self):
        result = []
        allAm = models.storage.all(Amenity)
        for x, y in allAm.items():
            if x.split('.')[1] in self.amenity_ids:
                result.append(y)

    @amenities.setter
    def amenities(self, x):
        if x.__name__ == Amenity:
            self.amenity_ids.append(x.id)
