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

app.secret_key = 'a sample key!!!!!!! llllll'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# moment = Moment(app)

from . import tea_web
from . import tea_api
from . import models
from . import db_config
from .models import db
