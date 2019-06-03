from user import User_CRUD
from flask_restful import Api

def init_resources(app):
    api = Api(app)
    api.add_resource(User_CRUD,"/user")
    return app

