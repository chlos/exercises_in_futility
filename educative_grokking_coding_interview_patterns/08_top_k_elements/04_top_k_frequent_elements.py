from heapq import heappush, heappushpop
import collections

def top_k_frequent(arr, k):
    freqs = collections.Counter(arr)

    top_k = []  # min heap
    for element, freq in freqs.items():
        if len(top_k) < k:
            heappush(top_k, (freq, element))
        else:
            heappushpop(top_k, (freq, element))

    return [element for freq, element in top_k]