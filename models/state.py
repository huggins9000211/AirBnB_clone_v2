#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
import models.city
import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        name = ''

        @property
        def cities(self):
            """ cities getter """
            result = []
            allStates = models.storage.all(models.city.City)
            for x, y in allStates.items():
                if y.state_id == self.id:
                    result.append(y)
            return result
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete', backref='state')
