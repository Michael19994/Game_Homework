from turtle import title
from flask import render_template
from app import app
from models.list_of_events import events
from models.event import *


@app.route('/events')
def index():
    return render_template('index.html', title='Homepage', events=events)