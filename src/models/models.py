from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields, Schema
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class tb_producto(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    referencia = db.Column(db.String(10), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    fecha_creacion = db.Column(db.String(20), default=datetime.now())
    dias_inventario = db.Column(db.Integer, nullable=False)
    cantidad_ventas = db.Column(db.Integer, nullable=False)


class ProductoSchema(SQLAlchemySchema):
    class Meta:
        model = tb_producto
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    nombre = fields.String()
    referencia = fields.String()
    precio = fields.Integer()
    peso = fields.Integer()
    categoria = fields.String()
    inventario = fields.Integer()
    fecha_creacion = fields.String()
    dias_inventario = fields.Integer()
    cantidad_ventas = fields.Integer()


class Inventariochema(SQLAlchemySchema):
    class Meta:
        model = tb_producto
        include_relationships = True
        include_fk = True
        load_instance = True

    nombre = fields.String()
    inventario = fields.Integer()


class Ventaschema(SQLAlchemySchema):
    class Meta:
        model = tb_producto
        include_relationships = True
        include_fk = True
        load_instance = True

    nombre = fields.String()
    cantidad_ventas = fields.Integer()
