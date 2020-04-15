#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = ''

        if not s or not t:
            return result

        counter_dict = [0 for _ in xrange(128)]
        for ch in t:
            counter_dict[ord(ch)] += 1

        left = 0
        right = 0
        count = len(t)
        min_left = left
        min_len = float('inf')

        while right < len(s):
            if counter_dict[ord(s[right])] > 0:
                count -= 1
            counter_dict[ord(s[right])] -= 1
            right += 1

            while count == 0:
                if (right - left < min_len):
                    min_left = left
                    min_len = right - left

                if counter_dict[ord(s[left])] >= 0:
                    count += 1
                counter_dict[ord(s[left])] += 1
                left += 1

        if min_len < float('inf'):
            print min_left, min_len
            result = s[min_left:min_left + min_len]
        return result
