from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/test?user=postgres&password=mbp'
db = SQLAlchemy(app)

from app import views, models