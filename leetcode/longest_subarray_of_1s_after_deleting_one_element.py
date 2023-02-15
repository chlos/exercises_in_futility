class Solution:

    # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/708201/java-python-3-sliding-window-with-at-most-one-zero-w-detailed-explanation-and-brief-analysis/

    # shrinking sliding window
    #
    # * [1111]
    #   window_sum == right - left + 1
    # * [1101]
    #   window_sum == right - left
    # * [1001]
    #   window_sum < right - left
    def longestSubarray_shrink(self, nums: List[int]) -> int:
        result = 0

        window_sum = 0
        left, right = 0, 0
        for right in range(len(nums)):
            window_sum += nums[right]

            # shrink the window until we have only one zero inside
            while left < right and window_sum < right - left:
                window_sum -= nums[left]
                left += 1

            result = max(result, right - left)

        return result

    # sliding window
    def longestSubarray_nonShrink(self, nums: List[int]) -> int:
        result = 0

        window_sum = 0
        left, right = 0, 0
        for right in range(len(nums)):
            window_sum += nums[right]

            # shrink the window until we have only one zero inside
            if window_sum < right - left:
                window_sum -= nums[left]
                left += 1

            result = max(result, right - left)

        return result

    # DP
    # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/708109/python-o-n-dynamic-programming-detailed-explanation/
    def longestSubarray(self, nums):
        n = len(nums)
        if sum(nums) == n: return n - 1

        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = nums[0]

        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0], dp[i][1] = dp[i-1][0] + 1, dp[i-1][1] + 1
            else:
                dp[i][0], dp[i][1] = 0, dp[i-1][0]

        return max([i for j in dp for i in j])