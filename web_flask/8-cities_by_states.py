#!/usr/bin/python3
""" test """
from flask import Flask, escape, request, render_template
from models import storage, State, City
import os
import copy

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def hello():
    """ test """
    allStates = list(storage.all(State).values())
    allStates.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=allStates)


@app.teardown_appcontext
def dbColose(error):
    storage.close()


if __name__ == "__main__":
    app.run()
