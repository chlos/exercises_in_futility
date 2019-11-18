#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint


class ParseSexp(object):
    def __init__(self, sexp_str):
        self.sexp_tokenized = self._tokenize(sexp_str)
        self.parsed = self._parse()

    def get_parsed(self, pretty=False):
        return self.parsed

    def pretty_print(self):
        pprint.PrettyPrinter(indent=2).pprint(self.parsed)

    def _handle_scalar_value(self, value):
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        return str(value)

    def _tokenize(self, sexp_str):
        sexp_tokenized = sexp_str.replace('(', ' ( ').replace(')', ' ) ').split()
        return sexp_tokenized

    def _parse(self):
        current_node = self.sexp_tokenized.pop(0)
        if current_node == '(':
            nested_lists = []
            while self.sexp_tokenized[0] != ')':
                nested_lists.append(self._parse())
            else:
                self.sexp_tokenized.pop(0)

            return nested_lists
        else:
            return self._handle_scalar_value(current_node)


def test(parser):
    sexp = '(first (list 1.2 (+ 2 3) 9))'
    sexp_parsed = parser(sexp)
    sexp_parsed.pretty_print()
    assert sexp_parsed.get_parsed() == ['first', ['list', 1.2, ['+', 2, 3], 9]]


def main():
    test(ParseSexp)


if __name__ == '__main__':
    main()
