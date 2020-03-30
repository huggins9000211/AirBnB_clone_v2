#!/usr/bin/python3
"""This is the file storage class for AirBnB"""


class DBStorage():
    """ db """
    __engine = None
    __session = None

    def __init__(self):
        """ init """