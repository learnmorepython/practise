#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
practise_decorator
"""
import functools

# 装饰器
"""
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数
"""
# 不带参数的decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print "call %s():" % func.__name__
        return func(*args, **kw)
    return wrapper

# 把@log放到now()函数的定义处，相当于执行了now = log(now)
@log
def now():
    print "this is now"
now()


# 带参数的decorator
"""
首先执行log('execute')，返回的是decorator函数，
再调用返回的函数，参数是now函数，返回值最终是wrapper函数
"""
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print "%s %s():" % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# 相当于执行了now = log("execute")(now)
@log1("execute")
def now1():
    print "this is now1"
now1()