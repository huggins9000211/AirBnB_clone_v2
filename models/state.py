#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    def cities(self):
        """ cities getter """
        result = {}
        allStates = models.storage.all(State)
        for x, y in allStates.items():
            if y.state_id == self.id:
                result[x] = y
        return result
