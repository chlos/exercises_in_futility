import heapq


def find_kth_largest(arr, k):
    top_k = []
    for i in range(k):
        heapq.heappush(top_k, arr[i])
    for i in range(k, len(arr)):
        heapq.heappushpop(top_k, arr[i])

    return top_k[0]