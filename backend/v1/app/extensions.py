import os
from dotenv import load_env
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


load_env()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
paychangu_client = PaychanguClient(secret_key=os.getenv("PAYCHANGU_SECRET_KEY"))