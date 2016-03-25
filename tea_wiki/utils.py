from functools import wraps
from flask import g

def PERMISSION(PERMISSION_LIMIT):
    '''
    根据函数创建装饰器，得到不同的权限装饰器
    '''
    def permission_dec(func):
        @wraps
        def f():
            if g.user and g.user.permission >= PERMISSION_LIMIT:
                return func()
            else:
                pass
        return f
    return permission_dec
