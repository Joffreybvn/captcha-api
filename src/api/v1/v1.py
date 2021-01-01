
# Initialize this sub-modules as a Flask blueprint
from flask import Blueprint
from flask_restx import Api

# Import the routes
from src.api.v1 import captcha

blueprint = Blueprint('v1', __name__)

# Merge the blueprints with the doc
api = Api(blueprint,
          title='Captcha API',
          version='1.0',
          description='Demo API made with flask and flask-restX.')

api.add_namespace(captcha.api)
