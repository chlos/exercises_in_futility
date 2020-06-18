#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

if __name__ == '__main__':
    filename = 'strings.txt'
    with open(filename, 'r') as in_file:
        for line_number, line in enumerate(in_file, 1):
            line = line.strip()
            try:
                nums = line.split()
                if nums:
                    print(sum(map(float, nums)))
                else:
                    print(line)
            except ValueError:
                print('Error: {}'.format(line_number), file=sys.stderr)
