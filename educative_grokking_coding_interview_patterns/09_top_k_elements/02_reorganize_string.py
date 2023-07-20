class Solution:
    def reorganizeString(self, s: str) -> str:
        # count chars freqs
        chars_freq = collections.Counter(s)

        # store freqs in max heap
        max_heap = []
        for ch, freq in chars_freq.items():
            heapq.heappush(max_heap, (-freq, ch))

        # build result
        result = ''
        prev = None
        while max_heap or prev:
            # incorrect input case: we don't have more chars
            # but we still have repeating char in "prev" (aaab)
            if prev and not max_heap:
                return ''

            freq, ch = heapq.heappop(max_heap)
            freq = -freq    # remember: we store negative freqs to emulate max heap
            result += ch
            freq -= 1

            # we push the char back to the max heap during the next iteration
            # to avoid repetition during the push with decreased freq
            if prev is not None:
                heapq.heappush(max_heap, prev)
                prev = None
            if freq > 0:
                prev = -freq, ch

        return result