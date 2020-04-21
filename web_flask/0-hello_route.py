""" test """
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ test """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
