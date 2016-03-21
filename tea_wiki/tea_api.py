'''
    提供手机api
'''
import json
from flask import g, jsonify, request
from flask.ext.restful import Api, Resource
from flask.ext.httpauth import HTTPBasicAuth
from . import app, api, auth
from .models import User
#api = Api(app)
#auth = HTTPBasicAuth()


class tea_news_list(Resource):
    '''
    tea news list
    '''

    decorators = [auth.login_required]

    def get(self,news_type):
        return {1:1}


api.add_resource(tea_news_list, '/news_list/<int:news_type>')


class tea_news(Resource):
    '''
    tea news api for cellphone
    '''
    decorators = [auth.login_required]

    def get(self, id):
        pass


api.add_resource(tea_news, '/news/<int:id>')


@app.route('/api/news_list/<int:news_type>', methods = ['GET'])
@auth.login_required
def get_news_list():
    return str(news_type)

@app.route('/api/news/<int:news_id>', methods = ['GET'])
@auth.login_required
def get_news():
    pass


@app.route('/api/token', methods = ['POST'])
@auth.login_required
def get_auth_token():
    token = g.user.get_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration':600})

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True
