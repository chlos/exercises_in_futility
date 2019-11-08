#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


def get_anagrams(words):
    word_groups = collections.defaultdict(list)
    for word in words:
        word_sorted = ''.join(sorted(word))
        word_groups[word_sorted].append(word)

    return word_groups


def main():
    words = ['a', 'b']
    print get_anagrams(words)
    words = ['a', 'b', 'ab', 'ba']
    print get_anagrams(words)
    words = ['a', 'b', 'aab', 'ba']
    print get_anagrams(words)


if __name__ == "__main__":
    main()
