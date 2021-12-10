from flask import Blueprint
from app.routes.pedidos import pedidos_ctrl

bp = Blueprint('pedidos_routes_bp', __name__, url_prefix='/api/pedidos')

@bp.route('/', methods=['GET'])
def get_pedidos():
    return pedidos_ctrl.get_pedidos()

@bp.route('/', methods=['POST'])
def post_pedido():
    return pedidos_ctrl.post_pedido()
