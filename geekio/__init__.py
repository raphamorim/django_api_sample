from flask import Flask
from flask.ext.script import Manager
from flask.ext import restful

app = Flask(__name__)
manager = Manager(app)
api = restful.Api(app)

import geekio.views
import geekio.resources
