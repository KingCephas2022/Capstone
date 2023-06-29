
from flask_migrate import Migrate
from flask import Flask
from extentions import db
import random
import string
from models import Url


#from flask_jwt_extended import JWTManager
#from flask_restx import Api
#from flask_cors import CORS


#************************************************
#APP INITIALIZATION
#************************************************

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #SQLite db file
    app.config['SECRET_KEY'] = 'capachino'
    app.config['BASE_URL'] = 'http://localhost:5000'
    app.config['URL_MAP'] = {}

    db.init_app(app)

    migrate = Migrate(app, db)

    return app

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # Generate a 6-character short URL
    
    # Check if the generated short URL already exists in the database
    existing_url = Url.query.filter_by(short_url=short_url).first()
    if existing_url:
        # If the short URL already exists, generate a new one recursively
        return generate_short_url()
    
    return short_url
















