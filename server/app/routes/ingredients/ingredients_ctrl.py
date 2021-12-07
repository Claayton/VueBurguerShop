from app.extensions.database import db
from flask import jsonify, request
from app.models.tables import Ingredient

def post_ingredient():
    ingrediente = request.json['ingrediente']
    tipo = request.json['tipo']
    ingredient = Ingredient(ingrediente, tipo)
    
    try:
        db.session.add(ingredient)
        db.session.commit()
        json_ingredient = {
                "id": ingredient.id,
                "name": ingredient.ingrediente,
                "tipo": ingredient.tipo
        }
        return jsonify({'message': 'Successfully registered', 'data': json_ingredient}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500
    
def get_ingredients():
    ingredients = Ingredient.query.all()
    json_ingredients = {}
    if ingredients:
        for ingredient in ingredients:
            json_ingredient = {
                "id": ingredient.id,
                "name": ingredient.ingrediente,
                "tipo": ingredient.tipo
            }
            json_ingredients[json_ingredient["id"]]=json_ingredient
            
        return jsonify({'message': 'Successfully fetched', 'data': json_ingredients}), 200
    return jsonify({'message': 'nothing found', 'data': {}}), 404

def delete_ingredient(id:int):
    ingredient = Ingredient.query.filter_by(id=id).first()
    
    if not ingredient:
        return jsonify({'message': "Ingredient don't exist", 'data': {}}), 403
    
    else:
        json_ingredient = {
            "id": ingredient.id,
            "name": ingredient.ingrediente,
            "tipo":ingredient.tipo
        }
    
    try:
        db.session.delete(ingredient)
        db.session.commit()
        return jsonify({'message': 'Sucessfully deleted', 'data': json_ingredient}), 200
    except:
        return jsonify({'message': 'Unable to delete', 'data': json_ingredient}), 500
