#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def qsort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    arr_less = [e for e in arr[1:] if e <= pivot]
    arr_greater = [e for e in arr[1:] if e > pivot]
    return qsort(arr_less) + [pivot] + qsort(arr_greater)


def test(f):
    arr_0 = []
    assert f(arr_0) == []
    arr_1 = [1]
    assert f(arr_1) == [1]
    arr_2_sorted = [1, 2]
    assert f(arr_2_sorted) == [1, 2]
    arr_2_unsorted = [2, 1]
    assert f(arr_2_unsorted) == [1, 2]
    arr_big = [10, 5, 4, 2, 9, -12, 2, 1]
    assert f(arr_big) == [-12, 1, 2, 2, 4, 5, 9, 10]

    arr_random = [random.randint for x in xrange(100)]
    assert f(arr_random) == sorted(arr_random)


def main():
    test(qsort)
    print 'OK'


if __name__ == "__main__":
    main()
