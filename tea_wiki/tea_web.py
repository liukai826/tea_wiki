'''
    提供web后台管理界面
'''

from . import app


@app.route('/')
def index():
    return 'hello'
