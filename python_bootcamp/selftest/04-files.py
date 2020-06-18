#!/usr/bin/env python
# -*- coding: utf-8 -*-

lens = []
fname_in = 'example.txt'
with open(fname_in, 'r') as f:
    for line in f:
        lens.append(str(len(line.split())) + '\n')

fname_out = 'result.txt'
with open(fname_out, 'w') as f:
    f.writelines(lens)
