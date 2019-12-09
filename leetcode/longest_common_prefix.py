#!/usr/bin/env python
# -*- coding: utf-8 -*-


def longestCommonPrefix1(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ''
    current_index = 0

    while strs:
        current_char = previous_char = ''
        for word in strs:
            if current_index < len(word):
                if current_char:
                    previous_char = current_char
                current_char = word[current_index]
                if previous_char and current_char != previous_char:
                    return prefix
            else:
                return prefix
        prefix += current_char
        current_index += 1
    return prefix


def longestCommonPrefix2(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    curr_index = 0
    for curr_chars in zip(*strs):
        if len(set(curr_chars)) > 1:
            break
        else:
            curr_index += 1
    return strs[0][:curr_index]


def test(func):
    print func(['foobar', 'foobar'])
    print func(['foobar', 'barbaz'])
    print func(['f', 'fo', 'foo'])
    assert func([]) == ''


def main():
    test(longestCommonPrefix1)
    test(longestCommonPrefix2)

if __name__ == "__main__":
    main()
