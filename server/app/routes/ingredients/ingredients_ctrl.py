from app.extensions.database import db
from flask import jsonify, request
from app.models.tables import Ingredient

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

def post_ingredient():
    ingrediente = request.json['ingrediente']
    tipo = request.json['tipo']
    ingredient = Ingredient(tipo, ingrediente)
    
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
    
def update_ingredient(id:int):
    ingredient = Ingredient.query.filter_by(id=id).first()
    
    if not ingredient:
         return jsonify({'message': "Ingredient not found", 'data': {}}), 404
    
    try:
        ingredient.ingrediente = request.json['ingrediente']
        ingredient.tipo = request.json['tipo']
        db.session.commit()
        json_ingredient = {
                "id": ingredient.id,
                "name": ingredient.ingrediente,
                "tipo": ingredient.tipo
        }
        return jsonify({'message': 'Successfully registered', 'data': json_ingredient}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500
    
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

def get_paes():
    paes = Ingredient.query.filter_by(tipo="pão").all()
    json_paes = {}
    if paes:
        for pao in paes:
            json_pao = {
                "id": pao.id,
                "name": pao.ingrediente,
                "tipo": pao.tipo
            }
            json_paes[json_pao["id"]]=json_pao
            
        return jsonify({'message': 'Successfully fetched', 'data': json_paes}), 200
    return jsonify({'message': 'nothing found', 'data': {}}), 404

def post_pao():
    ingredient = request.json['ingrediente']
    tipo = 'pão'
    pao = Ingredient(tipo, ingredient)
    
    try:
        db.session.add(pao)
        db.session.commit()
        json_pao = {
                "id": pao.id,
                "name": pao.ingrediente,
                "tipo": pao.tipo
        }
        return jsonify({'message': 'Successfully registered', 'data': json_pao}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500

def get_carnes():
    carnes = Ingredient.query.filter_by(tipo="carne").all()
    json_carnes = {}
    if carnes:
        for carne in carnes:
            json_carne = {
                "id": carne.id,
                "name": carne.ingrediente,
                "tipo": carne.tipo
            }
            json_carnes[json_carne["id"]]=json_carne
            
        return jsonify({'message': 'Successfully fetched', 'data': json_carnes}), 200
    return jsonify({'message': 'nothing found', 'data': {}}), 404

def post_carne():
    ingredient = request.json['ingrediente']
    tipo = 'carne'
    carne = Ingredient(tipo, ingredient)
    
    try:
        db.session.add(carne)
        db.session.commit()
        json_carne = {
                "id": carne.id,
                "name": carne.ingrediente,
                "tipo": carne.tipo
        }
        return jsonify({'message': 'Successfully registered', 'data': json_carne}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500

def get_opcionais():
    opcionais = Ingredient.query.filter_by(tipo="opcional").all()
    json_opcionais = {}
    if opcionais:
        for opcional in opcionais:
            json_opcional = {
                "id": opcional.id,
                "name": opcional.ingrediente,
                "tipo": opcional.tipo
            }
            json_opcionais[json_opcional["id"]]=json_opcional
            
        return jsonify({'message': 'Successfully fetched', 'data': json_opcionais}), 200
    return jsonify({'message': 'nothing found', 'data': {}}), 404

def post_opcional():
    ingredient = request.json['ingrediente']
    tipo = 'opcional'
    opcional = Ingredient(tipo, ingredient)
    
    try:
        db.session.add(opcional)
        db.session.commit()
        json_opcional = {
                "id": opcional.id,
                "name": opcional.ingrediente,
                "tipo": opcional.tipo
        }
        return jsonify({'message': 'Successfully registered', 'data': json_opcional}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500
