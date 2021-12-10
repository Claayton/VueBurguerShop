from app.extensions.database import db
from flask import jsonify, request
from app.models.tables import Pedido

def get_pedidos():
    pedidos = Pedido.query.all()
    json_pedidos = {}
    if pedidos:
        for pedido in pedidos:
            json_pedido = {
                "id": pedido.id,
                "name": pedido.nome,
                "carne": pedido.carne,
                "pão": pedido.pao,
                "opcionais": pedido.opcionais
            }
            json_pedidos[json_pedido["id"]]=json_pedido
            
        return jsonify({'message': 'Successfully fetched', 'data': json_pedidos}), 200
    return jsonify({'message': 'nothing found', 'data': {}}), 404

def post_pedido():
    name = request.json['name']
    carne = request.json['carne']
    pao = request.json['pao']
    opcionais = request.json['opcionais']
    
    pedido = Pedido(name, carne, pao, opcionais)
    
    try:
        db.session.add(pedido)
        db.session.commit()
        json_pedido = {
                "id": pedido.id,
                "name": pedido.nome,
                "carne": pedido.carne,
                "pão": pedido.pao,
                "opcionais": pedido.opcionais
        }
        return jsonify({'message': 'Successfully registered', 'data': json_pedido}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500
