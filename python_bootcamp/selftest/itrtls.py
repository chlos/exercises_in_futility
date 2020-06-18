#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
chars = ["C", "D", "E", "F", "G", "A", "H"]
for c, s in itertools.izip_longest(chars, itertools.repeat("", 2), fillvalue="#"):
    print c + s
