'''
    提供web后台管理界面
'''
from datetime import datetime

from flask.ext.moment import Moment as moment
from flask import render_template, request, abort
from .models import User, News
from . import app


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(error):
    title = str(error)
    msg = error.description
    return render_template('errors.html',
                        title=title,
                        message=msg)
