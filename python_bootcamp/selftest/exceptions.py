#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    print("First")
    raise KeyError()
    print "Second"
except RuntimeError:
    print "Third"
except KeyError:
    print "Fourth"
finally:
    print "Fifth"
