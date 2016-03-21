from . import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
app.config['SECRET_KEY'] = 'secret key'
db = SQLAlchemy(app)
