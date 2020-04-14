#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s2 or not s1 or len(s2) < len(s1):
            return False

        counter_dict = [0 for _ in xrange(128)]
        for ch in s1:
            counter_dict[ord(ch)] += 1

        left = 0
        right = 0
        count = len(s1)
        while right < len(s2):
            # move right border
            if counter_dict[ord(s2[right])] >= 1:
                # we are getting closer to s1-anagram
                count -= 1
            counter_dict[ord(s2[right])] -= 1
            right += 1

            # check the current window
            if count == 0:
                return True

            # move left border
            if right - left == len(s1):
                if counter_dict[ord(s2[left])] >= 0:
                    # we are getting further to s1-anagram
                    count += 1
                counter_dict[ord(s2[left])] += 1
                left += 1

        return False
