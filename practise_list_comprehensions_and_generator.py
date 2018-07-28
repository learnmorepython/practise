#!/usr/bin/python
# -*- coding: utf-8 -*-
"""practise_list_comprehensions_and_generator"""

# list_comprehensions
# 老方法生成列表
L = []
for x in range(1, 11):
    L.append(x * x)
print L

# 列表生成器
print [x * x for x in range(1, 11)]

# 可以加上if判断
print [x * x for x in range(1, 11) if x % 2 == 0]

# 使用双层循环
print [m + n for m in "ABC" for n in "XYZ"]

# 使用dirc用列表生成器生成list
d = {"x": "A", "y": "B", "c": "C"}
print [k + "=" + v for k, v in d.iteritems()]

L = ["Hello", "World", "IBM"]
print [x.lower() for x in L]

# generator
g = (x * x for x in range(1, 11))
print g
# 打印出generator的元素
for n in g:
    print n

# 生成器函数
"""
1/生成器函数包含一个或者多个yield
2/当调用生成器函数时，函数将返回一个对象，但是不会立刻向下执行
3/像__iter__()和__next__()方法等是自动实现的，所以我们可以通过next()方法对对象进行迭代
4/一旦函数被yield，函数会暂停，控制权返回调用者
5/局部变量和它们的状态会被保存，直到下一次调用
6/函数终止的时候，StopIteraion会被自动抛出
"""
def my_gen():
    n = 1
    print "first"
    # yield区域
    yield n

    n += 1
    print "second"
    yield n

    n += 1
    print "third"
    yield n

a = my_gen()
print "next method:"
# 每次调用a的时候，函数都从之前保存的状态执行
print next(a)
print next(a)
print next(a)

print "for loop:"
b = my_gen()
for elem in b:
    print elem


# 逆序yield出对象的元素
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

for char in rev_str("hello"):
    print char

