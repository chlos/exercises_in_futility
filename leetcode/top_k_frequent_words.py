#!/usr/bin/env python3

# more ideas: https://leetcode.com/problems/top-k-frequent-words/solutions/431008/summary-of-all-the-methods-you-can-imagine-of-this-problem/

import collections
import heapq


class Pair():
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.freq

    def __lt__(self, other):
        if self.freq == other.freq:
            # lexic order of words
            return self.word > other.word
        return self.freq < other.freq


class Solution:
    # sort; nlog(n)
    def topKFrequent_sort(self, words: List[str], k: int) -> List[str]:
        freqs = collections.Counter(words)

        pairs = []
        for word, freq in freqs.items():
            pairs.append((freq, word))
        pairs = sorted(pairs, key=lambda pair: (-pair[0], pair[1]))
        # print(pairs)

        return [pairs[i][1] for i in range(k)]

	# min heap / priority queue
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = collections.Counter(words)

        freqs_heap = []
        heapq.heapify(freqs_heap)
        for word, freq in freqs.items():
            heapq.heappush(freqs_heap, Pair(freq, word))
            if len(freqs_heap) > k:
                heapq.heappop(freqs_heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(freqs_heap).word)

        return result[::-1]
