from functools import wraps

def LOGIN(func):
    @wraps
    def f():

        return func()
    return f
