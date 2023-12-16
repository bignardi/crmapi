import os


SECRET_KEY = os.urandom(32)

DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))

from  api.database import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS