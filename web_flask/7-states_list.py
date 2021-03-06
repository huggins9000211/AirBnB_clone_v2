#!/usr/bin/python3
""" test """
from flask import Flask, escape, request, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello():
    """ test """
    allStates = list(storage.all(State).values())
    allStates.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', statelist=allStates)


@app.teardown_appcontext
def dbColose(error):
    storage.close()


if __name__ == "__main__":
    app.run()
