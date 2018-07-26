#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
practise_function
"""


def power(x, n=2):
    """默认参数"""
    s = 1
    while n > 0:
        s = x * s
        n -= 1
    print s


power(2)
power(2, 5)


def calc(*number):
    """可变参数, args接收的是一个tuple"""
    sum = 0
    for n in number:
        sum = sum + n * n
    print sum


L = [1, 3, 5]
calc(1, 2)
calc(*L)


def person(name, age, **kw):
    """关键字参数, kw接收的是一个dict"""
    print "name:", name, "age:", age, "other:", kw


extra = {"city": "beijing", "job": "engineer"}
person("jack", 24, **extra)


def func(a, b, c = 0, *args, **kw):
    """组合参数"""
    print "a=", a, "b=", b, "c=", c, "args=", args, "kw=", kw


func(1, 2,)
func(1, 2, c=3)
func(1, 2, 3, "a", "b")
func(1, 2, 3, "a", "b", x=99)
args = (1, 2, 3, 4)
kw = {"x": 99}
func(4, 3, 1, *args, **kw)
