from flask import Flask
from extensions import jwt, db, migrate


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


    return app