#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findAnagramsSortedSlices(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        sorted_p = sorted(p)
        result = []
        for i in xrange(len(s)):
            if sorted_p == sorted(s[i:i + len(p)]):
                result.append(i)

        return result

    def findAnagramsNSquareDict(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        p_chars = defaultdict(int)
        for ch in p:
            p_chars[ch] += 1

        result = []
        for i in xrange(len(s)):
            if s[i] not in p_chars:
                continue

            curr_chars = defaultdict(int)
            i_end = i + len(p) if i + len(p) < len(s) else len(s)
            for j in xrange(i, i_end):
                if s[j] not in p_chars:
                    break
                curr_chars[s[j]] += 1

            if curr_chars == p_chars:
                result.append(i)

        return result

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if not s or not p or len(s) < len(p):
            return result

        counter_dict = [0 for _ in xrange(128)]
        for ch in p:
            counter_dict[ord(ch)] += 1

        left = 0
        right = 0
        count = len(p)
        while right < len(s):
            # move right border
            if counter_dict[ord(s[right])] >= 1:
                # we are getting closer to p-anagram
                count -= 1
            counter_dict[ord(s[right])] -= 1
            right += 1

            # check the current window
            if count == 0:
                result.append(left)

            # move left border
            if right - left == len(p):
                if counter_dict[ord(s[left])] >= 0:
                    # we are getting further to p-anagram
                    count += 1
                counter_dict[ord(s[left])] += 1
                left += 1

        return result


s = Solution()
assert s.findAnagrams('cbaebabacd', 'abc') == [0, 6]
assert s.findAnagrams('abab', 'ab') == [0, 1, 2]
print 'Tests OK'
