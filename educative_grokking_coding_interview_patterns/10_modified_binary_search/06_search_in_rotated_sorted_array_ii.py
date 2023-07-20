class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            # skip duplicates
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2
            if nums[mid] == target:
                return True

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

        return False