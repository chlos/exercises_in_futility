class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left side is sorted
            if nums[left] <= nums[mid]:
                # target is somewhere in the left side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                # target is outside of the left side
                else:
                    left = mid + 1
            # right side is sorted
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1