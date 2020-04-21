#!/usr/bin/python3
""" test """
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ test """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ test """
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def hello(text):
    """ test """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
