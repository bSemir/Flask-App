from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# creating a key to config so flask could know where the db is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '589403d8cbe7f71dcce91f08'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# tell the login_manager where's login route located, this is enough to redirect to /login instead of /market
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes

# every python package that is considered as a regular package includes __init__ file
# if we want to import something, before it imports, __init__ executes
