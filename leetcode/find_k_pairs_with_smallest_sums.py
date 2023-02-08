import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_sums = []

        for i1 in range(len(nums1)):
            heapq.heappush(min_sums, (nums1[i1] + nums2[0], i1, 0))

        result = []
        count = 0
        while min_sums and count < k:
            _, i1, i2 = heapq.heappop(min_sums)

            result.append((nums1[i1], nums2[i2]))

            next_i2 = i2 + 1
            if next_i2 < len(nums2):
                heapq.heappush(min_sums, (nums1[i1] + nums2[next_i2], i1, next_i2))

            count += 1

        return result