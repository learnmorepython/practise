#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
practise_dict_and_set
"""

# dict：初始化后可以修改
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print "d is:", d
print "d['Bob']:", d["Bob"]
d["Bob"] = 90
print "d is:", d
print "d['Bob']:", d["Bob"]
print "get Jack:", d.get("Jack", 60)
d.pop("Bob")
print "after pop d is:", d
# 迭代key
for key in d:
    print "this is iterkey", key

# 迭代value
for value in d.itervalues():
    print "this is itervalues:", value

# 迭代key和value
for k, v in d.iteritems():
    print "this is iterkey", k, "and itervalue:", v


# set：无序和无重复元素的集合
s = set([1, 1, 2, 2, 3, 3])
print s
s.add(4)
s.add(4)
print "after add twice:", s
s.remove(4)
print "after remove:", s

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print "s1 & s2:", s1 & s2
print "s1 | s2:", s1 | s2


