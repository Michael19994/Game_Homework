import unittest
from app import app

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/<name>")
def welcome(name):
    return f"Hello, {name}!"