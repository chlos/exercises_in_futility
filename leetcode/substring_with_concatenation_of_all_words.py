#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []

        if not s or not words:
            return result

        words_count = Counter(words)
        words_num = len(words)
        word_len = len(words[0])

        for i in xrange(len(s) - words_num * word_len + 1):
            curr_count = defaultdict(int)
            for j in xrange(i, i + words_num * word_len, word_len):
                curr_word = s[j:j + word_len]
                if curr_word in words_count:
                    curr_count[curr_word] += 1
                    if curr_count[curr_word] > words_count[curr_word]:
                        break
                else:
                    break

            if curr_count == words_count:
                result.append(i)

        return result


s = Solution()
assert s.findSubstring('barfoothefoobarman', ["foo", "bar"]) == [0, 9]
print 'OK'
