from flask import Blueprint

bp = Blueprint("test_route_bp", __name__)

@bp.route('/')
def hello_world():
    return '<h1>Helo World piazada!</h1>'
