#coding:utf-8
'''
    提供手机api
'''
import json
from flask import g, jsonify, request
from flask.ext.restful import Api, Resource
from flask.ext.httpauth import HTTPBasicAuth
from . import app, api, auth
from .models import *
#api = Api(app)
#auth = HTTPBasicAuth()


# class tea_news_list(Resource):
#     '''
#     tea news list
#     '''
#
#     decorators = [auth.login_required]
#
#     def get(self,news_type):
#         return {1:1}
#
#
# api.add_resource(tea_news_list, '/api/news_list/<int:news_type>')
#
#
# class tea_news(Resource):
#     '''
#     tea news api for cellphone
#     '''
#     decorators = [auth.login_required]
#
#     def get(self, id):
#         pass
#
#
# api.add_resource(tea_news, '/api/news/<int:id>')


@app.route('/api/news_list/<int:news_type>', methods = ['GET'])
# @auth.login_required
def get_news_list(news_type):
    news_list = News.query.filter_by(news_type = news_type).all()
    news_data = [{'id':info.id, 'title':info.title, 'author':info.author} for
                 info in news_list]
    return jsonify(news_data)

@app.route('/api/news/<int:news_id>', methods = ['GET'])
# @auth.login_required
def get_news(news_id):
    news = News.query.filter_by(id = news_id).first()
    news_data = {'id': news.id, 'title': news.title, 'content': news.content}
    return jsonify(news_data)


@app.route('/api/token', methods = ['POST'])
# @auth.login_required
def get_auth_token():
    token = g.user.get_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration':600})

@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
