class Solution:
    # https://leetcode.com/problems/continuous-subarray-sum/solutions/236976/python-solution/comments/1199456
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_mods = {0: -1}
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]

            if k != 0:
                curr_mod = cum_sum % k
            else:
                curr_mod = cum_sum

            if curr_mod in prefix_mods:
                prev_mod_i = prefix_mods[curr_mod]
                if i - prev_mod_i > 1:
                    return True
            else:
                prefix_mods[curr_mod] = i

        return False

# p.s.: brute force: https://leetcode.com/problems/continuous-subarray-sum/solutions/99518/not-smart-solution-but-easy-to-understand/