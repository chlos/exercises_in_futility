#!/usr/bin/env python
# -*- coding: utf-8 -*-

mylist = range(12)
mylist = map(lambda x: x*2, filter(lambda x: x < 5, mylist))
print mylist

strings = map(str, range(64))
print strings
