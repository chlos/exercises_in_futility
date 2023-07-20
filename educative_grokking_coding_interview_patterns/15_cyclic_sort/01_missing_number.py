class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # cycle sort
        i = 0
        while i < len(nums):
            n = nums[i]

            if n == i or n >= len(nums):
                i += 1
                continue

            nums[i], nums[n] = nums[n], nums[i]

        # detect missing num
        for i, n in enumerate(nums):
            if i != n:
                return i
        return len(nums)