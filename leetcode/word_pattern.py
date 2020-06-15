#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}
        for idx, word in enumerate(words):
            pattern_char = pattern[idx]
            expected_word = char_to_word.get(pattern_char)
            if (expected_word or word_to_char.get(word)) and expected_word != word:
                return False

            char_to_word[pattern_char] = word
            word_to_char[word] = pattern_char

        return True

s = Solution()
assert s.wordPattern('abba', 'dog cat cat dog') == True
assert s.wordPattern('abba', 'dog cat cat fish') == False
assert s.wordPattern('abba', 'dog dog dog dog') == False
assert s.wordPattern('aaa', 'aa aa aa aa') == False
