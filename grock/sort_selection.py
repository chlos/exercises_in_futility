#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_min_idx(arr):
    min_idx = 0
    for i, x in enumerate(arr):
        if x < arr[min_idx]:
            min_idx = i
    return min_idx


def selection_sort_1(arr):
    sorted_arr = []
    for i in xrange(len(arr)):
        min_el = arr.pop(get_min_idx(arr))
        sorted_arr.append(min_el)

    return sorted_arr


def selection_sort_2(arr):
    for i in xrange(len(arr)):
        min_idx = i
        for j in xrange(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


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


def main():
    test(selection_sort_1)
    test(selection_sort_2)
    print 'OK'


if __name__ == "__main__":
    main()
