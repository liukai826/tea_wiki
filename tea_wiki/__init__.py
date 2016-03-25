from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.restful import Api
from flask.ext.httpauth import HTTPBasicAuth
# from flask.ext.moment import Moment
from flask.ext.login import LoginManager

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
Bootstrap(app)
login_manager = LoginManager()
login_manager.init__app(app)
# moment = Moment(app)

from . import tea_web
from . import tea_api
from . import models
from . import db_config
from .models import db
