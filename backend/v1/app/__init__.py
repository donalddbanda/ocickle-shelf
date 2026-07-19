from flask.globals import current_app
from flask import Flask
from extensions import jwt, db, migrate


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # server_environment = current_app.config["FLASK_ENV"]
    # if server_environment == "production"

    return app