from src import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .models import db
from .views import views

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(views.ViewProducts, '/products')
api.add_resource(views.ViewInventory, '/inventory')
api.add_resource(views.ViewSell, '/sell')
api.add_resource(views.ViewProduct, '/products/<int:id_producto>')
api.add_resource(views.ViewPong, '/ping')


jwt = JWTManager(app)
