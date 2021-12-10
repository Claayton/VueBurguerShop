"""Diretódio de tabelas de pedidos"""
from app.extensions.database import db


class Ingredient(db.Model):
    """Tabela de Ingredientes"""
    __tablename__ = 'ingredientes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    ingrediente = db.Column(db.String(100), nullable=False)

    def __init__(self, tipo:str, ingrediente:str):
        self.tipo = tipo
        self.ingrediente = ingrediente

    def __repr__(self):
        return f'<Ingrediente {self.ingrediente}'


class Pedido(db.Model):
    """Tabela de pedidos"""
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    carne = db.Column(db.String(100), nullable=False)
    pao = db.Column(db.String(100), nullable=False)
    opcionais = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, carne, pao, opcionais):
        self.nome = nome
        self.carne = carne
        self.pao = pao
        self.opcionais = opcionais

    def __repr__(self):
        return f'Pedido {self.id}'


class Status(db.Model):
    """Tabela de status do pedido"""
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)

    pedido = db.relationship('Pedido', foreign_keys=pedido_id)

    def __init__(self, tipo):
        self.tipo = tipo

    def __repr__(self):
        return f'<Status {self.tipo}'


class Opcional(db.Model):
    """Tabela de Opcionais"""
    __tablename__ = 'opcionais'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tipo =  db.Column(db.String(100), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)

    pedido = db.relationship('Pedido', foreign_keys=pedido_id)

    def __init__(self, tipo):
        self.tipo = tipo

    def __repr__(self):
        return f'<Opcional {self.tipo}'
