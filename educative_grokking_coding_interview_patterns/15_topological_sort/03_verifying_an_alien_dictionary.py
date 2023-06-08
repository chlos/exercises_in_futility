#!/usr/bin/env python3


from types import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {ch: i for i, ch in enumerate(order)}

        for word_i in range(len(words) - 1):
            curr_word = words[word_i]
            next_word = words[word_i + 1]
            for ch_i in range(len(curr_word)):
                if ch_i >= len(next_word):
                    # first word is bigger that the second one (it breaks the sorted order)
                    return False
                if curr_word[ch_i] == next_word[ch_i]:
                    # equal chars
                    continue
                if order_map[curr_word[ch_i]] < order_map[next_word[ch_i]]:
                    # this pair is in sorted order, check the next pair
                    break
                else:
                    # this pair is not in sorted order, words ar not sorted
                    return False

        return True
