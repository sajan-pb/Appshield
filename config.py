import os

class Config:

    SECRET_KEY = "dev-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///appshield.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False