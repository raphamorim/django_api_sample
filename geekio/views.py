from flask import render_template
from geekio import app, api

@app.route('/')
def index():
    return render_template('index.html', endpoints=api.endpoints) 
