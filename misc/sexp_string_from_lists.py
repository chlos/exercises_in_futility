#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_sexp_str(sexp):
    result = ''
    if isinstance(sexp, list):
        result += '(' + ' '.join(get_sexp_str(exp) for exp in sexp) + ')'
    else:
        result += str(sexp)

    return result


def main():
    sexp_lists = ['+', 3, ['*', 2, ['+', 5, 9]]]
    result = get_sexp_str(sexp_lists)
    print result
    assert result == '(+ 3 (* 2 (+ 5 9)))'

    sexp_lists = ['+', ['-', 10, 12], ['*', 2, ['+', 5, 9]]]
    result = get_sexp_str(sexp_lists)
    print result
    assert result == '(+ (- 10 12) (* 2 (+ 5 9)))'

    print 'OK'


if __name__ == "__main__":
    main()
