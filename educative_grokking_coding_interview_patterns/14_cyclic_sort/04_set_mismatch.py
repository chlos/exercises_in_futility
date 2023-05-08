class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # cyclic sort
        i = 0
        while i < len(nums):
            i_val = nums[i]

            if i_val - 1 == i:
                i += 1
                continue

            if nums[i_val - 1] == i_val:
                i += 1
                continue
            nums[i], nums[i_val - 1] = nums[i_val - 1], nums[i]

        # find a dup on the wrong position i; there must be missing N=i+1 number
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]

        return [-1, -1]