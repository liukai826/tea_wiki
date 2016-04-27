# coding:utf-8

'''
    提供web后台管理界面
'''
from datetime import datetime

from flask import render_template, request, abort, redirect
from flask.ext.login import login_required
from .models import User, News
from . import app, auth
from . import utils
from .forms import *



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('base.html')
    else:
        pass


@app.route('/manage/news', methods=['GET', 'POST'])
# @auth.login_required
def manage_news():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('manage_news.html')
    else:
        pass


@app.route('/manage/news_type', methods=['GET', 'POST'])
# @auth.login_required
def manage_news_type():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('manage_type.html')
    else:
        pass


@app.route('/manage/api_user', methods=['GET', 'POST'])
# @auth.login_required
def manage_api_user():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('manage_api.html')
    else:
        pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    elif request.method == 'GET':
        pass
    else:
        pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    title = str(error)
    msg = error.description
    return render_template('errors.html',
                        title=title,
                        message=msg)
