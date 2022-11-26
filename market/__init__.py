from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# creating a key to config so flask could know where the db is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes

# every python package that is considered as a regular package includes __init__ file
# if we want to import something, before it imports, __init__ executes
