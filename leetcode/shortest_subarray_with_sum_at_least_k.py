import collections

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solutions/245363/a-template-for-monotonic-queue-problems/
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solutions/204290/monotonic-queue-summary/
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solutions/2251761/monotonic-queue-explanation/
# https://1e9.medium.com/monotonic-queue-notes-980a019d5793
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # list of all [0...i] sums
        sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]

        result = len(nums) 
        mono_deque = collections.deque()    # indexes
        for i in range(len(nums) + 1):
            # remove all prefix sums higher than current sum 
            # as they won't be used now or after since this index will be shorter
            while mono_deque and sums[mono_deque[-1]] > sums[i]:
                mono_deque.pop()

            # check each element which satisfies K sum condition (sums[l] <= sums[r] - K)
            # and remove it as it won't be used in afterwards 
            # since current window will always be smaller
            while mono_deque and sums[i] - sums[mono_deque[0]] >= k:
                result = min(result, i - mono_deque[0])
                mono_deque.popleft()

            mono_deque.append(i)

        if result < len(nums):
            return result
        if sums[len(nums)] < k:
            return -1
        else:
            return len(nums)