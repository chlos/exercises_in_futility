class Solution:
    # greedy
    # https://leetcode.com/problems/jump-game-ii/solutions/485780/python-java-js-c-o-n-sol-based-on-greedy-of-coverage-with-explanation/
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        num_jumps = 0
        last_jump_i = 0
        curr_coverage = 0
        dest_i = len(nums) - 1
        for i in range(len(nums)):
            # extend current coverage
            curr_coverage = max(curr_coverage, i + nums[i])

            # we have to jump again
            if i == last_jump_i:
                last_jump_i = curr_coverage
                num_jumps += 1
                # finish reached
                if last_jump_i >= dest_i:
                    return num_jumps

        return num_jumps