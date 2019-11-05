#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bin_search(data, value):
    lo = 0
    hi = len(data)
    while lo <= hi:
        mid = (lo + hi) / 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def main():
    d3 = [1, 2, 3]
    print bin_search(d3, 1)
    print bin_search(d3, 2)
    print bin_search(d3, 3)
    d4 = [1, 2, 3, 4]
    print bin_search(d4, 1)
    print bin_search(d4, 2)
    print bin_search(d4, 3)
    print bin_search(d4, 4)


if __name__ == "__main__":
    main()
