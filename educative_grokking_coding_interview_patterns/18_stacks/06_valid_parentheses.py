#!/usr/bin/env python
# -*- coding: utf-8 -*-


brackets_map = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_stack = []
        for bracket in s:
            if bracket in brackets_map.iterkeys():
                # open bracket
                brackets_stack.append(bracket)
            elif bracket in brackets_map.itervalues():
                # close bracket
                try:
                    last_open_bracket = brackets_stack.pop()
                except IndexError:
                    # close bracket without open one
                    return False
                if bracket != brackets_map[last_open_bracket]:
                    return False

        if not brackets_stack:
            return True
