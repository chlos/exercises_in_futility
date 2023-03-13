class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            # mid is index of 1st element of some pair (if it's a "good" part of array)
            # or mid is index of the 2nd element of some pair (if it's "bad" part)
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                # it was "good" sub-array, search for single elem in the "bad" one
                left = mid + 2

        return nums[left]