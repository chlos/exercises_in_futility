#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bin_search(data, value):
    lo = 0
    hi = len(data) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def bin_search_recursive(data, value):
    def recurse(lo, hi):
        mid = (lo + hi) / 2
        if lo > hi:
            return None
        elif data[mid] < value:
            return recurse(mid + 1, hi)
        elif data[mid] > value:
            return recurse(lo, mid - 1)
        else:
            return mid
    return recurse(0, len(data) - 1)


def bin_search_recursive_bool(data, value):
    if len(data) == 0:
        return False

    lo = 0
    hi = len(data) - 1
    mid = (lo + hi) / 2
    if data[mid] == value:
        return True
    elif data[mid] < value:
        return bin_search_recursive_bool(data[mid + 1:], value)
    else:
        return bin_search_recursive_bool(data[:mid], value)


def test(f):
    d0 = []
    assert f(d0, -1) == None
    assert f(d0, 1) == None
    d1 = [1]
    assert f(d1, -1) == None
    assert f(d1, 1) == 0
    assert f(d1, 2) is None
    d2 = [1, 2]
    assert f(d2, -1) == None
    assert f(d2, 1) == 0
    assert f(d2, 2) == 1
    assert f(d2, 3) is None
    d3 = [1, 2, 3]
    assert f(d3, -1) == None
    assert f(d3, 1) == 0
    assert f(d3, 2) == 1
    assert f(d3, 3) == 2
    assert f(d3, 4) is None
    d4 = [1, 2, 3, 4]
    assert f(d3, -1) == None
    assert f(d4, 1) == 0
    assert f(d4, 2) == 1
    assert f(d4, 3) == 2
    assert f(d4, 4) == 3
    assert f(d3, 5) is None


def test_bool(f):
    d0 = []
    assert f(d0, -1) == False
    assert f(d0, 1) == False
    d1 = [1]
    assert f(d1, -1) == False
    assert f(d1, 1) == True
    assert f(d1, 2) is False
    d2 = [1, 2]
    assert f(d2, -1) == False
    assert f(d2, 1) == True
    assert f(d2, 2) == True
    assert f(d2, 3) is False
    d3 = [1, 2, 3]
    assert f(d3, -1) == False
    assert f(d3, 1) == True
    assert f(d3, 2) == True
    assert f(d3, 3) == True
    assert f(d3, 4) is False
    d4 = [1, 2, 3, 4]
    assert f(d3, -1) == False
    assert f(d4, 1) == True
    assert f(d4, 2) == True
    assert f(d4, 3) == True
    assert f(d4, 4) == True
    assert f(d3, 5) is False


def main():
    test(bin_search)
    test(bin_search_recursive)
    test_bool(bin_search_recursive_bool)
    print 'OK'


if __name__ == "__main__":
    main()
