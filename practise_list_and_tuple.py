#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
practise_list_and_tuple
"""

# list：初始化后可以修改
classmates = ["jone", "mike", "bob"]
print "classmates is:", classmates
print "len is:", len(classmates)
print "first is:", classmates[0], ",second is:", classmates[1], ",third is:", classmates[2]
print "first is:", classmates[-3], ",second is:", classmates[-2], ",third is:", classmates[-1]
classmates[1]= "jim"
print "classmates is:", classmates
classmates_new = ["tom", "bak"]
classmates.insert(2, classmates_new)
print "after insert list classmates is:", classmates
classmates.append("lei")
print "after append classmates is:", classmates
classmates.insert(2, "jack")
print "after insert classmates is:", classmates
classmates.pop()
print "after pop classmates is:", classmates
classmates.pop(2)
print "after pop index classmates is:", classmates
classmates.extend(classmates_new)
print "after extend classmates is:", classmates
print "classmates[2][0]:", classmates[2][0]
print "classmates[:]", classmates[:], ",classmates[2:4]", classmates[2:4]

# 每隔2个取一个
print "classmates[::2]", classmates[::2]

# 迭代list
for l in classmates:
    print l

# 迭代list的索引和元素
for i, value in enumerate(["A", "B", "C"]):
    print i, value

for x, y in [(3, 2), (4, 1), (5, 4)]:
    print x, y


# tuple：初始化后不能修改
classmates_tuple = ("jone", "mike", "bob")
print "classmates_tuple is:", classmates_tuple
print "classmates_tuple[2]:", classmates_tuple[2]
print "classmates_tuple[:]:", classmates_tuple[:], ",classmates_tuple[-3:-1]:", classmates_tuple[-3:-1]

