#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    # brute force
    def countSubstringsBruteForce(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in xrange(len(s)):
            print 'i: ', i
            count += 1
            substring = s[i]
            print substring
            for j in xrange(1, len(s) - i):
                print 'j: ', j
                substring += s[i + j]
                if self.isPalindrome(substring):
                    count += 1
                print substring, self.isPalindrome(substring)

        return count

    def countPalindromes(self, s, i, j):
        count = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
        return count

    # expanse to odd/even palindromes
    def countSubstringsExpand(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        for i in xrange(len(s)):
            count += self.countPalindromes(s, i, i)
            count += self.countPalindromes(s, i, i + 1)

        return count

    # DP
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp_table = [[False for _ in xrange(n)] for _ in xrange(n)]
        count = 0

        for i in xrange(n - 1, -1, -1):
            dp_table[i][i] = True
            count += 1
            for j in xrange(i + 1, len(s)):
                # Check for a window of size 2
                if j == i + 1 and s[i] == s[j]:
                    dp_table[i][j] = True
                    count += 1
                # Check for a window of size 3+
                if j > i + 1 and dp_table[i + 1][j - 1] and s[i] == s[j]:
                    dp_table[i][j] = True
                    count += 1

        return count


s = Solution()
assert s.countSubstrings('a') == 1
assert s.countSubstrings('abc') == 3
assert s.countSubstrings('aa') == 3
assert s.countSubstrings('aaa') == 6
print 'OK'
