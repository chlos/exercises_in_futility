#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Filter adjacent matching lines from INPUT, writing to
OUTPUT. With no options, matching lines are merged to
the first occurrence.
"""

import argparse
import contextlib
import sys


def get_args():
    parser = argparse.ArgumentParser(
        prog='uniq - report or omit repeated lines',
        description=__doc__
    )
    parser.add_argument(
        "in_file",
        help="INPUT",
        nargs="?",
        type=str
    )
    parser.add_argument(
        "out_file",
        help="OUTPUT",
        nargs="?",
        type=str
    )
    parser.add_argument(
        "-c", "--count",
        action="store_true",
        help="prefix lines by the number of occurrences"
    )
    parser.add_argument(
        "-d", "--repeated",
        action="store_true",
        help="only print duplicate lines"
    )
    parser.add_argument(
        "-i", "--ignore-case",
        action="store_true",
        help="ignore differences in case when comparing"
    )
    parser.add_argument(
        "-u", "--unique",
        action="store_true",
        help="only print unique lines"
    )
    return parser.parse_args()


def write_line_if_needed(args, out_file, prev_line, count):
    if args.count:
        prev_line = '{c} {s}'.format(c=count, s=prev_line)
    if (not args.repeated and not args.unique
            or args.repeated and count > 1
            or args.unique and count == 1):
        out_file.write(prev_line)


@contextlib.contextmanager
def open_file_or_std(mode, filename=None):
    if mode == 'r':
        std_pipe = sys.stdin
    elif mode == 'w':
        std_pipe = sys.stdout
    else:
        raise ValueError('Wrong mode {!r}. Only "r" and "w" allowed'.format(mode))

    if filename and filename != '-':
        with open(filename, mode) as file_object:
            yield file_object
    else:
        yield std_pipe


def handle_line(line, ignore_case):
    if ignore_case:
        return line.lower()
    else:
        return line


def main():
    args = get_args()

    if args.repeated and args.unique:
        return

    with open_file_or_std('r', args.in_file) as in_file, \
            open_file_or_std('w', args.out_file) as out_file:
        if args.repeated and args.unique:
            return

        prev_line = in_file.readline()
        count = 1

        for curr_line in in_file:
            if handle_line(curr_line, args.ignore_case) == handle_line(prev_line, args.ignore_case):
                count += 1
            else:
                # new unique line found
                write_line_if_needed(args, out_file, prev_line, count)
                count = 1
            prev_line = curr_line
        write_line_if_needed(args, out_file, prev_line, count)


if __name__ == '__main__':
    main()
