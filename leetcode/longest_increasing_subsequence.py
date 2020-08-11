#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programmingc
class Solution:
    # N^2
    # https://e-maxx.ru/algo/longest_increasing_subseq_log
    def lengthOfLIS_n2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # max subseq nums[0]...nums[i] lens
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    # NlogN
    # https://e-maxx.ru/algo/longest_increasing_subseq_log
    # https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_tails = [0] * len(nums)
        size = 0
        for num in nums:
            i = 0
            j = size
            while i != j:
                mid = (i + j) // 2
                if dp_tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            dp_tails[i] = num
            size = max(i + 1, size)
        return size


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print('OK')