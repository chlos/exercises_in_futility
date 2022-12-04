class Solution:
    # backtracking
    # time: O(n**2)
    # space: O(n) -- recursion
    def canJump_backtracking(self, nums: List[int]) -> bool:
        def canJumpFromPos(pos, nums):
            # we reached the last index, hooray
            if pos == len(nums) - 1:
                return True

            furthest_pos = min(pos + nums[pos], len(nums) - 1)
            next_pos = pos + 1
            while next_pos <= furthest_pos:
                if canJumpFromPos(next_pos, nums):
                    return True
                next_pos += 1

            return False

        return canJumpFromPos(0, nums)

    # backtracking + DP (top down)
    # time: O(n**2)
    # space: O(n) -- recursion
    def canJump_dpTopDown(self, nums: List[int]) -> bool:
        BAD = -1
        UNKNOWN = 0
        GOOD = 1
        memo = [UNKNOWN] * len(nums)
        memo[len(nums) - 1] = GOOD

        def canJumpFromPos(pos, nums):
            # we reached the last index, hooray
            if memo[pos] != UNKNOWN:
                return memo[pos] == GOOD

            furthest_pos = min(pos + nums[pos], len(nums) - 1)
            next_pos = pos + 1
            while next_pos <= furthest_pos:
                if canJumpFromPos(next_pos, nums):
                    memo[pos] = GOOD
                    return True
                next_pos += 1

            memo[pos] = BAD
            return False

        return canJumpFromPos(0, nums)

    # backtracking + DP (bottom up)
    # time: O(n**2)
    # space: O(n) -- recursion
    def canJump_dpBootomUp(self, nums: List[int]) -> bool:
        BAD = -1
        UNKNOWN = 0
        GOOD = 1
        memo = [UNKNOWN] * len(nums)
        memo[len(nums) - 1] = GOOD

        for pos in reversed(range(len(nums) - 1)):
            furthest_pos = min(pos + nums[pos], len(nums) - 1)
            for i in range(pos + 1, furthest_pos + 1):
                if memo[i] == GOOD:
                    memo[pos] = GOOD
                    break

        return memo[0] == GOOD

    # greedy
    # time: O(n)
    # space: 1
    def canJump(self, nums: List[int]) -> bool:
        # we'll move backwards from the last index
        goodPosition = len(nums) - 1
        for i in reversed(range(len(nums))):
            # check if we can reach the previous "good" position
            if i + nums[i] >= goodPosition:
                goodPosition = i
        
        return goodPosition == 0
