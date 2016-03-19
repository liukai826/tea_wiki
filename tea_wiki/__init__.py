from flask import Flask


app = Flask(__name__)

from . import tea_web
from . import tea_api
from . import models
