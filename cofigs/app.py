from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config,Development

app=Flask(__name__)

app.config.from_object(Development)
db=SQLAlchemy(app)
@app.route('/')
def index():
    return 'Hello'