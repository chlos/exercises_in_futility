#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_groups = defaultdict(list)
        for str in strs:
            str_key = ''.join(sorted(str))
            str_groups[str_key].append(str)
        return [str_group for str_group in str_groups.itervalues()]


def main():
    solution = Solution()
    assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["tan", "nat"], ["bat"], ["eat", "tea", "ate"]]


if __name__ == "__main__":
    main()
