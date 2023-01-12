class Solution:

    # slow/fast pointers: https://leetcode.com/problems/circular-array-loop/solutions/2242470/slow-and-fast-pointer-python/
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            # taking a step here means returning to the same location
            if nums[i] == len(nums):
                continue

            is_forward = nums[i] >= 0
            fast_ptr = i
            slow_ptr = i
            while slow_ptr != fast_ptr or slow_ptr != -1 or fast_ptr != -1:
                # move slow ptr one step
                slow_ptr = self.nextIndex(nums, slow_ptr, is_forward)
                if slow_ptr == -1:
                    break
                
                # move fast ptr two steps
                fast_ptr = self.nextIndex(nums, fast_ptr, is_forward)
                if fast_ptr != -1:
                    fast_ptr = self.nextIndex(nums, fast_ptr, is_forward)
                if fast_ptr == -1 or fast_ptr == slow_ptr:
                    break
            
            # loop found; direction was not changed
            if slow_ptr == fast_ptr and slow_ptr != -1:
                return True

        return False

    # return the next step or -1 in case if direction is changed
    def nextIndex(self, nums, ptr, is_forward):
        next_direction = (nums[ptr] >= 0)
        if next_direction != is_forward:
            return -1

        next_index = (ptr + nums[ptr]) % len(nums)
        if next_index == ptr:
            return -1

        return next_index