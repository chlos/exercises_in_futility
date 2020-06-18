#!/usr/bin/env python
# -*- coding: utf-8 -*-

numbers = ("1", "2", "3")
gnumbers = (i for i in numbers)


def fnumbers():
    for val in numbers:
        yield val

print "\t".join(numbers)
print "\t".join(gnumbers)
print "\t".join(fnumbers())
