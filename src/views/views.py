from flask_restful import Resource
from ..models import db, tb_producto, ProductoSchema, Inventariochema, Ventaschema

producto_schema = ProductoSchema()
inventario_schema = Inventariochema()
venta_schema = Ventaschema()


class ViewProducts(Resource):
    def get(self):
        try:
            return [producto_schema.dump(product) for product in tb_producto.query.all()], 200

        except Exception as e:
            return {'message': 'Something went wrong'}, 500


class ViewProduct(Resource):

    def get(self, id_producto):
        try:
            return producto_schema.dump(tb_producto.query.get_or_404(id_producto)), 200

        except Exception as e:
            return {'message': 'Something went wrong'}, 500


class ViewInventory(Resource):
    def get(self):
        try:
            return [inventario_schema.dump(product) for product in tb_producto.query.all()], 200

        except Exception as e:
            return {'message': 'Something went wrong'}, 500


class ViewSell(Resource):
    def get(self):
        try:
            return [venta_schema.dump(product) for product in tb_producto.query.all()], 200

        except Exception as e:
            return {'message': 'Something went wrong'}, 500


class ViewPong(Resource):

    def get(self):
        return {'message': 'Api Cafeteria works!'}, 200
