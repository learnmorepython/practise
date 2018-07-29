#!/usr/bin/python
# -*- coding: utf-8 -*-
"""practise_higher_order_function"""

x = abs(-10)
print x
y = abs
print y(-10)

# 高阶函数：函数接收另一个函数作为参数
def add(a, b, c):
    return c(a) + c(b)

print add(-5, 6, abs)

# python内建了map和reduce，filter,sorted函数
"""
map()函数接收两个参数，一个是函数，一个是序列，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
"""
def f(x):
    return x * x
print "map:", map(f, [1, 2, 3, 4, 5, 6, 7, 8])

# 把list的数字转化为字符串
print "map:", map(str, [1, 2, 3, 4, 5, 6])

"""
reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算, 
效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
def fn(x, y):
    return x * 10 + y
print "reduce:", reduce(fn, [1, 3, 5, 7, 9])


"""
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
"""
def is_odd(n):
    return n % 2 == 1
print "filter:", filter(is_odd, [1, 2, 4, 5, 6, 9])


# sorted
print "sorted:", sorted([35, 8, 14, 2])

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print "sorted:", sorted(["bob", "about", "Zoo", "Credit"], cmp_ignore_case)

# 匿名函数, 用lambda定义，冒号前的x表示函数参数
print "lambda:", map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7])

# 利用变量来调用
f = lambda x: x * x
print f(5)

# 匿名函数作为返回值返回
def build(x, y):
    return lambda: x * y + y * y
print build(2, 4)
