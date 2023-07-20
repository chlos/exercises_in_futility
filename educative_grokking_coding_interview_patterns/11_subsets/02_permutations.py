class Solution:
    def permute_recur(self, nums, start_idx, result):
        # base case
        if start_idx == len(nums) - 1:
            result.append(nums)
            return

        for i in range(start_idx, len(nums)):
            nums_copy = nums[:]
            nums_copy[start_idx], nums_copy[i] = nums_copy[i], nums_copy[start_idx]
            self.permute_recur(nums_copy, start_idx + 1, result)


    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.permute_recur(nums, 0, result)

        return result