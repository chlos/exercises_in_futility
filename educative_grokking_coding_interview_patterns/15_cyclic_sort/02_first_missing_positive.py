class Solution:
    # sort
    # O(n logn)
    def firstMissingPositive_sort(self, nums: List[int]) -> int:
        nums.sort()

        expected_positive = 1
        for n in nums:
            if n == expected_positive:
                expected_positive += 1

        return expected_positive

    # hashset
    def firstMissingPositive_hashset(self, nums: List[int]) -> int:
        nums_set = {n: True for n in nums}

        for expected_positive in range(1, len(nums) + 1):
            if expected_positive not in nums_set:
                return expected_positive
        return max(nums) + 1

    # cyclic sort
    # O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cyclic sort for positive numbers
        for i in range(len(nums)):
            correct_i = nums[i] - 1
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[correct_i]:
                nums[i], nums[correct_i] = nums[correct_i], nums[i]
                correct_i = nums[i] - 1

        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1