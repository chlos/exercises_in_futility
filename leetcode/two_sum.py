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


def test(f):
    assert f([3, 2, 4], 6) == (1, 2)
    print 'OK'


def main():
    test(twoSum)


if __name__ == "__main__":
    main()
