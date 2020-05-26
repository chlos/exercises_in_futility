#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def count_seq(arr):
    # print '===== arr:', arr
    return len(set(arr))


def main():
    count = None
    arr_len = None
    for n in sys.stdin:
        if count is None:
            count = int(n.strip())
        elif count > 0:
            if arr_len is None:
                arr_len = n
            else:
                arr = [int(e) for e in n.split()]
                seq_len = count_seq(arr)
                print seq_len
                count -= 1
                arr_len = None
        else:
            break


if __name__ == "__main__":
    main()
