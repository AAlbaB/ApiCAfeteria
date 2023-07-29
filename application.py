from src import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from src.models import db
from src.views import views

application = create_app('default')
app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()
cors = CORS(application)

api = Api(application)
api.add_resource(views.ViewProduct, '/products/<int:id_producto>')
api.add_resource(views.ViewProducts, '/products')
api.add_resource(views.ViewInventory, '/inventory')
api.add_resource(views.ViewSell, '/sell')
api.add_resource(views.ViewPong, '/')


jwt = JWTManager(application)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
