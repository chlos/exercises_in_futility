# knapsack problem
# https://leetcode.com/discuss/study-guide/1152328/01-Knapsack-Problem-and-Dynamic-Programming
# https://leetcode.com/discuss/study-guide/1308617/Dynamic-Programming-Patterns

class Solution:
    # brute force; dfs
    def canPartition_bruteDFS(self, nums: List[int]) -> bool:
        def dfs(nums, i, sum_remaining):
            # base case: success
            if sum_remaining == 0:
                return True

            # failed to find the proper subset
            if i == 0 or sum_remaining < 0:
                return False

            return (
                # consider i-th element as a part of subset
                dfs(nums, i - 1, sum_remaining - nums[i]) or
                # don't consider
                dfs(nums, i - 1, sum_remaining)
            )

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        return dfs(nums, len(nums) - 1, subset_sum)

    # dfs + memoization (top down)
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums, i, sum_remaining):
            # base case: success
            if sum_remaining == 0:
                return True

            # failed to find the proper subset
            if i == 0 or sum_remaining < 0:
                return False

            return (
                # consider i-th element as a part of subset
                dfs(nums, i - 1, sum_remaining - nums[i]) or
                # don't consider
                dfs(nums, i - 1, sum_remaining)
            )

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        return dfs(tuple(nums), len(nums) - 1, subset_sum)

    # bottom up / DP
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        return dp[n][subset_sum]