#!/usr/bin/python3
"""test for db storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    '''this will test the DB storage'''

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_engine(self):
        """Tests engine connection"""
        pass

    def test_storage(self):
        """Tests storage"""
        pass

if __name__ == "__main__":
    unittest.main()
