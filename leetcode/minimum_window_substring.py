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


# more concise
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''

        # count hashmaps
        t_count = collections.Counter(t)
        window_count = collections.defaultdict(int)

        # condition counters of unique symbols (with required freq)
        # if we need to have AAA then t_count[A] == window_count[A] == 3; curr_n += 1
        required_n = len(t_count)
        curr_n = 0 

        # results
        l_result, r_result = None, None
        result_len = float('inf')

        l = 0
        # sliding window
        for r in range(len(s)):
            window_count[s[r]] += 1

            # upd current unique chars count
            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                curr_n += 1

            # adjusting sliding window, when all symbols found
            while curr_n == required_n:
                # update current result
                if (r - l + 1) < result_len:
                    l_result, r_result = l, r
                    result_len = r - l + 1
                # shrink window from left
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    curr_n -= 1
                l += 1

        if l_result is not None and r_result is not None:
            return s[l_result:r_result + 1]
        return ''