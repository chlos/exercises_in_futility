#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Print newline, word counts for a FILE.
NOTE: At least one keyword argument needed
"""

import argparse
import contextlib
import sys


class WcResult(object):
    def __init__(self, n_lines, n_words, n_chars, max_line_length):
        self.n_lines = n_lines
        self.n_words = n_words
        self.n_chars = n_chars
        self.max_line_length = max_line_length


def get_args():
    parser = argparse.ArgumentParser(
        prog='wc - print the number of newlines, words in files',
        description=__doc__
    )
    parser.add_argument(
        "in_file",
        help="FILE",
        nargs="?",
        type=str
    )
    parser.add_argument(
        "-m", "--chars",
        action="store_true",
        help="print the character counts"
    )
    parser.add_argument(
        "-l", "--lines",
        action="store_true",
        help="print the newline counts"
    )
    parser.add_argument(
        "-L", "--max-line-length",
        action="store_true",
        help="print the length of the longest line"
    )
    parser.add_argument(
        "-w", "--words",
        action="store_true",
        help="print the word counts"
    )

    args = parser.parse_args()
    if not any([args.chars, args.lines, args.max_line_length, args.words]):
        parser.print_help()
        return
    return args


def count_txt(input_iterator):
    n_lines = n_words = n_chars = max_line_length = 0
    for line in input_iterator:
        n_lines += 1
        n_words += len(line.split())
        n_chars += len(line)
        max_line_length = max(max_line_length, len(line.rstrip('\n')))
    return WcResult(n_lines, n_words, n_chars, max_line_length)


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


def get_values_to_print(
    print_lines, print_words, print_chars, print_max_line_length,
    wc_result
):
    values_to_print = []
    if print_lines:
        values_to_print.append(wc_result.n_lines)
    if print_words:
        values_to_print.append(wc_result.n_words)
    if print_chars:
        values_to_print.append(wc_result.n_chars)
    if print_max_line_length:
        values_to_print.append(wc_result.max_line_length)
    return values_to_print


def main():
    args = get_args()
    if args is None:
        return

    with open_file_or_std('r', args.in_file) as in_file:
        wc_result = count_txt(in_file)

    values_to_print = get_values_to_print(
        args.lines, args.words, args.chars, args.max_line_length,
        wc_result
    )
    print ' '.join(map(str, values_to_print))


if __name__ == "__main__":
    main()
