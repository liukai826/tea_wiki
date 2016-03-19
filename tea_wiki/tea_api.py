'''
    提供手机api
'''

from . import app

@app.route('/news/list/<int:news_type>')
def get_news_list(news_type):
    return '%s' %news_type

@app.route('/news/<int:id>')
def get_news(id):
    return '%s' %id

