#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test(f):
    minefield = [
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
    ]
    print_minefield(minefield)
    fill_safe_squares(minefield)
    assert minefield == [
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
    ]
    print_minefield(minefield)
    print 'OK'
    print

    minefield = [
        [ 0, -1, -1, -1,  0],
        [ 0, -1,  0, -1,  0],
        [ 0, -1, -1, -1,  0],
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
    ]
    print_minefield(minefield)
    fill_safe_squares(minefield)
    assert minefield == [
        [ 2, -1, -1, -1,  2],
        [ 3, -1,  8, -1,  3],
        [ 2, -1, -1, -1,  2],
        [ 1,  2,  3,  2,  1],
        [ 0,  0,  0,  0,  0],
    ]
    print_minefield(minefield)
    print 'OK'
    print

    minefield = [
        [-1, -1, -1, -1,  -1],
        [-1,  0,  0,  0,  -1],
        [-1,  0,  0,  0,  -1],
        [-1,  0,  0,  0,  -1],
        [-1, -1, -1, -1,  -1],
    ]
    print_minefield(minefield)
    fill_safe_squares(minefield)
    assert minefield == [
        [-1, -1, -1, -1,  -1],
        [-1,  5,  3,  5,  -1],
        [-1,  3,  0,  3,  -1],
        [-1,  5,  3,  5,  -1],
        [-1, -1, -1, -1,  -1],
    ]
    print_minefield(minefield)
    print 'OK'
    print

    minefield = [
        [-1,  0,  0,  0,  0],
        [ 0, -1,  0,  0,  0],
        [ 0,  0, -1,  0,  0],
        [ 0,  0,  0,  0, -1],
        [ 0, -1,  0,  0, -1],
    ]
    print_minefield(minefield)
    fill_safe_squares(minefield)
    assert minefield == [
        [-1,  2,  1,  0,  0],
        [ 2, -1,  2,  1,  0],
        [ 1,  2, -1,  2,  1],
        [ 1,  2,  2,  3, -1],
        [ 1, -1,  1,  2, -1],
    ]
    print_minefield(minefield)
    print 'OK'
    print


def print_minefield(minefield):
    for line in minefield:
        line_to_print = ''
        for square in line:
            line_to_print += str(square) + '\t'
        print line_to_print
    print


def is_bounds_ok(minefield, x, y):
    y_size = len(minefield)
    x_size = len(minefield[0])
    if x < 0 or x >= x_size or y < 0 or y >= y_size:
        return False
    return True


def calc_mines_around(minefield, x, y):
    mines_count = 0
    delta_range = (-1, 0, 1)
    for dx in delta_range:
        for dy in delta_range:
            if is_bounds_ok(minefield, x + dx, y + dy):
                if minefield[y + dy][x + dx] == -1:
                    mines_count += 1
    return mines_count


def fill_safe_squares(minefield):
    y_size = len(minefield)
    x_size = len(minefield[0])
    for y in xrange(0, y_size):
        for x in xrange(0, x_size):
            if minefield[y][x] != -1:
                minefield[y][x] = calc_mines_around(minefield, x, y)


def main():
    test(fill_safe_squares)


if __name__ == "__main__":
    main()
