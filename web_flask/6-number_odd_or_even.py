#!/usr/bin/python3
""" test """
from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ test """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ test """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ test """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ test """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ test """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ test """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ test """
    status = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == "__main__":
    app.run()
