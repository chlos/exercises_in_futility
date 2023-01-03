class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_len = 0
        prefix_sum = 0
        sums_indexes = {}

        for i, num in enumerate(nums):
            prefix_sum += num

            # sum[0...i] = k
            if prefix_sum == k:
                max_len = i + 1 # add 1 because array indexes start from 0

            # there is (previously met) subarray with sum = k
            if prefix_sum - k in sums_indexes:
                max_len = max(max_len, i - sums_indexes[prefix_sum - k])

            # upd sums-indexes map only if there was no such prefix sum met previously
            # we check it bc we need to maintain the MAX subarray len
            if prefix_sum not in sums_indexes:
                sums_indexes[prefix_sum] = i

        return max_len