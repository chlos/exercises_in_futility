# https://leetcode.com/problems/number-of-great-partitions/solutions/2947979/python3-dp-simple-solution-with-steps-and-intuition/
# https://leetcode.com/problems/number-of-great-partitions/solutions/2948637/python3-recursive-iterative/
class Solution:
    # Notice in the problem description that k < 1000
    # while number of subsets of the array can go as high as 2^1000,
    # instead of thinking from the perspextive of iterating through each subset,
    # we should think about how to use this "k" to resolve the problem
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(nums)

        # Find the total number of invalid_partitions in the array
        # with their sums smaller than k
        @cache
        def dp(i, curr_sum):
            if i == n:
                return 1

            # do not include the current nums[i]
            remove = dp(i + 1, curr_sum)
            keep = 0

            # include the current nums[i]
            if curr_sum + nums[i] < k:
                keep = dp(i + 1, curr_sum + nums[i])

            return remove + keep

        # The result is 2^n - 2*invalid_partitions,
        # where 2^n is the total number of partitions,
        # and 2*invalid_partitions because the invalid_partition can be in group1 or group2
        invalid_partitions = dp(0, 0)
        res = pow(2, n) - 2 * invalid_partitions
        return max(res, 0) % mod