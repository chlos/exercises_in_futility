#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Find all conforming evidence numbers.
"""

import argparse
import collections


def get_args():
    parser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument(
        "-e", "--evidence",
        help="An evidence",
        action='append',
        type=str
    )
    parser.add_argument(
        "-n", "--number",
        help="A number",
        action='append',
        type=str
    )
    return parser.parse_args()


def get_uniques_list(l):
    return list(collections.OrderedDict.fromkeys(l))


def get_conform_counts(numbers, evidences):
    numbers_conform_count = collections.defaultdict(int)
    for number in numbers:
        number_chars = set(number)
        for evidence in evidences:
            if evidence.issubset(number_chars):
                numbers_conform_count[number] += 1
    return numbers_conform_count


def main():
    args = get_args()
    if not args.number or not args.evidence:
        return

    numbers = get_uniques_list(args.number)
    evidences = map(set, get_uniques_list(args.evidence))
    numbers_conform_count = get_conform_counts(numbers, evidences)

    if numbers_conform_count:
        best_conform_count = max(numbers_conform_count.itervalues())
        for number in numbers:
            if numbers_conform_count[number] == best_conform_count:
                print number


if __name__ == "__main__":
    main()
