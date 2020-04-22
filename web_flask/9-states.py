#!/usr/bin/python3
""" test """
from flask import Flask, escape, request, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def hello():
    """ test """
    allStates = list(storage.all(State).values())
    allStates.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', statelist=allStates)


@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """ test """
    allStates = list(storage.all(State).values())
    allStates.sort(key=lambda x: x.name)
    state = False
    for x in allStates:
        if x.id == id:
            state = x
    return render_template('9-states.html', state=state)

@app.teardown_appcontext
def dbColose(error):
    storage.close()


if __name__ == "__main__":
    app.run()
