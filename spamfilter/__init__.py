from flask_restplus import Api
from flask import Blueprint

TEST_VAR = 'TEST VAR'

blueprint = Blueprint('api', __name__)

from spamfilter.main.controller.spamfilter_controller import api as spamfilter_ns

api = Api(blueprint,
    title = 'Flask Restplus API Boiler Plate with JWT',
    version = '1.0',
    description = 'A boilerplate for flask restplus web services'
)

api.add_namespace(spamfilter_ns, path = '/spamfilter')
