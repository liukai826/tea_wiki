import time
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from .db_config import *


class User(db.Model):
    '''
    后台管理用户表
    '''
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    time = db.Column(db.Integer)

    def __init__(self, username, email = ''):
        self.username = username
        self.email = email
        self.time = int(time.time())

    def __str__(self):
        return 'user db model'

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, username, password):
        return pwd_context.verify(password, self.password) 
    
    def generate_auth_token(self, expiration = 600):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user


class News(db.Model):
    '''
    茶新闻
    '''
    __tablename__ = 'tea_news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    content = db.Column(db.Text)
    ctime = db.Column(db.Integer)
    author = db.Column(db.String(500))
    news_type = db.Column(db.Integer)

    def __init__(self, title, content, n_type=0):
        self.title = title
        self.content = content
        self.author = author
        self.ctime = int(time.time())
        self.news_type_id = n_type


class NewsType(db.Model):


    __tablename__ = 'news_type'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(500))
    type_id = db.Column(db.Integer)


    def __init__(self, type_id, type_name):
        self.type_id = type_id
        self.type_name = type_name
