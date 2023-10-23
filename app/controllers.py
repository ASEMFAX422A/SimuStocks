from .app import app
from flask import *

@app.route('/')
def index():
    return render_template('index.html')
