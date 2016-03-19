import time

from db_config import *
from . import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
db = SQLAlchemy(app)

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

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.time = int(time.time())

    def __str__(self):
        return 'user db model'


class News(db.Model):
    '''
    茶新闻
    '''
    __tablename__ = 'tea_news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    content = db.Column(db.String(100000))
    time = db.Column(db.Integer)

    def __init__(self):
        pass


