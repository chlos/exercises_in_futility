#!/usr/bin/env python


class Cat(object):
    tail = 10

    def __init__(self):
        self.whiskers = 1

    def __str__(self):
        return "%s %s" % (self.tail, self.whiskers)


begemot = Cat()
Cat.tail = 100500
tom = Cat()
print begemot
print tom
