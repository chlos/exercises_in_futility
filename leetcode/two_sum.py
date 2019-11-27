#!/usr/bin/env python
# -*- coding: utf-8 -*-


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if i1 == i2:
                    continue
                if n1 + n2 == target:
                    return i1, i2


def twoSumHash(nums, target):
    num_index_map = {}
    for i, n in enumerate(nums):
        num_index_map[n] = i
    for n, i in num_index_map.iteritems():
        complement = target - n
        if complement in num_index_map:
            return i, num_index_map[complement]


def test(f):
    f_result = f([3, 2, 4], 6)
    print f_result
    assert f_result == (1, 2)
    print 'OK'


def main():
    test(twoSum)
    test(twoSumHash)


if __name__ == "__main__":
    main()
