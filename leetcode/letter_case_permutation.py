#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        if not S:
            return result

        def dfs(s_temp, i):
            if len(s_temp) == len(S):
                result.append(s_temp)
                return
            if S[i].isalpha():
                dfs(s_temp + S[i].swapcase(), i + 1)
            dfs(s_temp + S[i], i + 1)

        dfs('', 0)
        return result
