from app.errors.config_errors import MissingCorsOrigins
from app.errors.config_errors import MissingSecretKey
import os
from dotenv import load_env
from .errors.config_errors import *

class Config:
    # ENVIRONMENT
    ENVIRONMENT=os.getenv("ENVIRONMENT", "development")

    # DATABASE
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # SECURITY
    SECRET_KEY=os.getenv("SECRET_KEY")
    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")

    # Errors
    if not SECRET_KEY:
        raise MissingSecretKey("SECRET KEY not provided")
    # if not JWT_SECRET_KEY:
    #     raise MissingJWTSecretKey("JWT SECRET KEY not provided")

class DevelopmentConfig(Config):
    # DATABASE
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", "sqlite:///app.db")

    # CORS
    CORS_ORIGINS = "http://localhost:5137,http://localhost:3000"


class ProductionConfig(Config):

    CORS_ORIGINS=os.getenv("CORS_ORIGINS")
    
    # Errors
    # if not CORS_ORIGINS:
    #     raise MissingCorsOrigins("CORS ORIGINS not provided")