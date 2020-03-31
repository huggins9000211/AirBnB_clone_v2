#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
import models.base_model
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.city import City
from models.user import User


class DBStorage():
    """ db """
    __engine = None
    __session = None
    allTypes = {"User": User, "State": State, "City": City, "Amenity":\
         Amenity, "Place": Place, "Review": Review}

    def __init__(self):
        """ init """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(os.getenv(
                'HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'), os.getenv(
                    'HBNB_MYSQL_HOST'), os.getenv(
                        'HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            models.base_model.Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """ all """
        results = {}
        if cls is None:
            for name, x in self.allTypes.items():
                for y in self.__session.query(x):
                    results["{}.{}".format(name, y.id)] = y
            return results
        for y in self.__session.query(self.allTypes[cls]):
            results["{}.{}".format(cls, y.id)] = y
        return results
    
    def new(self, obj):
        """ new """
        self.__session.add(obj)
    
    def save(self):
        """ save """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload """
        models.base_model.Base.metadata.create_all(self.__engine)
        sessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session()
