#!/usr/bin/env python3

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        abc_map = {}
        for i, ch in enumerate(order):
            abc_map[ch] = i

        prev_word = None
        for word in words:
            if prev_word is None:
                prev_word = word
                continue

            curr_len = min(len(prev_word), len(word))
            for i in range(curr_len):
                if abc_map[prev_word[i]] > abc_map[word[i]]:
                    return False
                elif abc_map[prev_word[i]] < abc_map[word[i]]:
                    break
                else:
                    if i == curr_len - 1 and len(prev_word) > len(word):
                        return False

            prev_word = word

        return True


s = Solution()

words = ['hello', 'leetcode']
order = 'hlabcdefgijkmnopqrstuvwxyz'
assert s.isAlienSorted(words, order)
print(words, 'OK')

words = ['word', 'world', 'row']
order = 'worldabcefghijkmnpqstuvxyz'
assert not s.isAlienSorted(words, order)
print(words, 'OK')

words = ['apple', 'app']
order = 'abcdefghijklmnopqrstuvwxyz'
assert not s.isAlienSorted(words, order)
print(words, 'OK')

words = ['kuvp', 'q']
order = 'ngxlkthsjuoqcpavbfdermiywz'
assert s.isAlienSorted(words, order)
print(words, 'OK')

words = [
    'zirqhpfscx', 'zrmvtxgelh', 'vokopzrtc', 'nugfyso', 'rzdmvyf',
    'vhvqzkfqis', 'dvbkppw', 'ttfwryy', 'dodpbbkp', 'akycwwcdog',
]
order = 'khjzlicrmunogwbpqdetasyfvx'
assert not s.isAlienSorted(words, order)
print(words, 'OK')