#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

urls = []
fname_in = 'regexp.in'
with open(fname_in, 'r') as f:
    for line in f:
        if re.match(r'^https:\/\/\S+bender\.\w+\.\w+$', line):
            urls.append(line)

fname_out = 'regexp.out'
with open(fname_out, 'w') as f:
    f.writelines(urls)
