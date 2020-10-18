import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = "Wroclaw"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'wbeapp.db')

SECRET_KEY = "3211ba53a554f65abf7a72af2af58a0b05bf563d"