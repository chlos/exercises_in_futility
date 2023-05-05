class Solution:
    # brute force: sort
    # O(n logn)
    def findDuplicate_sort(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return nums[i]

    # set
    # O(N)
    # space O(N)
    def findDuplicate_set(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)

    # negative marking - NOTE: it changes the input data!
    # O(N)
    def findDuplicate_negativeMarking(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n] < 0:
                return n
            nums[n] = -nums[n]

    # cyclic sorting - recursive
    # O(N)
    def findDuplicate_cyclicSortRec(self, nums: List[int]) -> int:
        def swap(n):
            # duplicate found
            if nums[n] == n:
                return n

            next_n = nums[n]
            nums[n] = n
            return swap(next_n)

        return swap(0)

    # cyclic sorting - iterative
    # O(N)
    #
    # we will bring the number from the next index to index 0 
    # and continue from there (effectively performing a swap)
    def findDuplicate_cyclicSortIter(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]

        return nums[0]

    # Floyd's Tortoise and Hare (Cycle Detection)
    def findDuplicate(self, nums: List[int]) -> int:
        # find the 1st intersection of two pointers
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # slow starts from 0; fast starts from intersection and now it moves slow
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast