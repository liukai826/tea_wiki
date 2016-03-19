from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from . import tea_web
from . import tea_api
from . import models
from . import db_config
