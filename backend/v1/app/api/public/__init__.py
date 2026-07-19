from flask import Blueprint

publiC_routes_bp = Blueprint("public", __name__)

from . import routes