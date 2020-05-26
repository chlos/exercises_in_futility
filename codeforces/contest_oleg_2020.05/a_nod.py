#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def gcd(a, b):
    if a % b == 0:
        return b
    if b % a == 0:
        return a

    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def lcm(a, b):
    return a * b / gcd(a, b)


def find_a_b(x):
    a, b = x - 1, 1
    while True:
        while True:
            if gcd(a, b) + lcm(a, b) == x:
                return a, b
            a += 1
        b += 1


def main():
    count = None
    for n in sys.stdin:
        n = int(n.strip())
        if count is None:
            count = n
        elif count > 0:
            a, b = find_a_b(n)
            print a, b
            count -= 1
        else:
            break


if __name__ == "__main__":
    main()
