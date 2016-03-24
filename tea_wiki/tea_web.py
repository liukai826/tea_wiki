'''
    提供web后台管理界面
'''
from datetime import datetime

from flask import render_template, request, abort
from .models import User, News
from . import app, moment, auth



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('index.html')
    else:
        pass


@app.route('/manage/news', methods=['GET', 'POST'])
@auth.login_required
def manage_news():

    return render_template('manage_news.html')

@app.route('/manage/news_type', methods=['GET', 'POST'])
@auth.login_required
def manage_news_type():
    return render_template('manage_type.html')


@app.route('/manage/api_user', methods=['GET', 'POST'])
@auth.login_required
def manage_api_user():
    return render_template('manage_api.html')

@app.errorhandler(404)
def page_not_found(error):
    title = str(error)
    msg = error.description
    return render_template('errors.html',
                        title=title,
                        message=msg)
