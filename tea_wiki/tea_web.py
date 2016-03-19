'''
    提供web后台管理界面
'''
from flask import render_template, request, abort
from .models import User, News 
from . import app


@app.route('/')
def index():
    pass

@app.errorhandler(404)
def page_not_found(error):
    title = str(error)
    msg = error.description
    return render_template('errors.html',
                        title=title,
                        message=msg)

