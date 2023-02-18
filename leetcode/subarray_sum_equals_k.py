class Solution:
    # bruteforce
    def subarraySum_brute(self, nums: List[int], k: int) -> int:
        count = 0

        for left in range(len(nums)):
            curr_sum = 0
            for right in range(left, len(nums)):
                curr_sum += nums[right]
                if curr_sum == k:
                    count += 1
                    continue

        return count

    # cumulative sum
    def subarraySum_cumulative(self, nums: List[int], k: int) -> int:
        count = 0

        cum_sum = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            cum_sum[i] = cum_sum[i - 1] + nums[i - 1]

        for left in range(len(nums)):
            for right in range(left + 1, len(nums) + 1):
                if cum_sum[right] - cum_sum[left] == k:
                    count += 1

        return count

    # prefix sums
    # https://leetcode.com/problems/subarray-sum-equals-k/solutions/1759711/python-simple-python-solution-using-prefixsum-and-dictionary/
    # more details in comments
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1
        curr_sum = 0

        for n in nums:
            curr_sum += n
            count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1

        return count