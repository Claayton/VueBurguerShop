from flask import Blueprint
from app.routes.ingredients import ingredients_ctrl

bp = Blueprint('ingredients_routes_bp', __name__, url_prefix='/api/ingredients')

@bp.route('/', methods=['GET'])
def get_ingredients():
    return ingredients_ctrl.get_ingredients()

@bp.route('/', methods=['POST'])
def post_ingredient():
    return ingredients_ctrl.post_ingredient()

@bp.route('/<int:id>/', methods=['PUT'])
def put_ingredient(id:int):
    return ingredients_ctrl.update_ingredient(id)

@bp.route('/<int:id>/', methods=['DELETE'])
def delete_ingredient(id:int):
    return ingredients_ctrl.delete_ingredient(id)

@bp.route('/paes/', methods=["GET"])
def get_paes():
    return ingredients_ctrl.get_paes()

@bp.route('/pao/', methods=['POST'])
def post_pao():
    return ingredients_ctrl.post_pao()

@bp.route('/carnes/', methods=["GET"])
def get_carnes():
    return ingredients_ctrl.get_carnes()

@bp.route('/carne/', methods=['POST'])
def post_carne():
    return ingredients_ctrl.post_carne()

@bp.route('/opcionais/', methods=["GET"])
def get_opcionais():
    return ingredients_ctrl.get_opcionais()

@bp.route('/opcional/', methods=['POST'])
def post_opcional():
    return ingredients_ctrl.post_opcional()
