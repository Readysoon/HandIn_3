from dotenv import load_dotenv
from os import environ

PLANETS_PER_PAGE = 4

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

SECRET_KEY = environ.get('SECRET_KEY')