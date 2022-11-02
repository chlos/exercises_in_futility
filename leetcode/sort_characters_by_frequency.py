# https://leetcode.com/problems/sort-characters-by-frequency/solutions/93420/java-o-n-bucket-sort-solution-o-nlogm-priorityqueue-solution-easy-to-understand/
# https://leetcode.com/problems/sort-characters-by-frequency/solutions/93404/c-o-n-solution-without-sort/
import collections
import heapq


class Solution:
    def frequencySort_sorted_with_key(self, s: str) -> str:
        freqs = collections.Counter(s)
        result = sorted(s, key=lambda x: (freqs[x], x), reverse=True)

        result = ''.join(result)
        return result

    def frequencySort_histogram(self, s: str) -> str:
        if not s:
            return ''

        freqs = collections.Counter(s)
        max_freq = max(freqs.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for ch, count in freqs.items():
            buckets[count].append(ch)

        result = []
        for i in range(max_freq, 0, -1):
            for ch in buckets[i]:
                result.append(ch * i)

        result = ''.join(result)
        return result

    def frequencySort(self, s: str) -> str:
        if not s:
            return ''

        freqs = collections.Counter(s)

        heap = [(-count, ch) for ch, count in freqs.items()]
        heapq.heapify(heap)

        result = []
        while heap:
            count, ch = heapq.heappop(heap)
            result.append(ch * (-count))

        result = ''.join(result)
        return result


s = Solution()
s.frequencySort('loveleetcode') == 'eeeelloovtcd'
s.frequencySort('aabbbbbc') == 'bbbbbaac'