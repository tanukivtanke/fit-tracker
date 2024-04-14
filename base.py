from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os.path import abspath

app = Flask(__name__, instance_path=abspath("instance"))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.jinja_env.cache = {}
db = SQLAlchemy(app)
