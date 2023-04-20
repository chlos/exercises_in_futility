I_COUNT = 0
I_MARK = 1


class Solution:
    # https://leetcode.com/problems/number-of-ways-to-earn-points/solutions/3258089/c-java-python3-short-top-down-dp-explained/
    def waysToReachTarget_topDown(self, target: int, types: List[List[int]]) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dfs(curr_type, target_remaining):
            if target_remaining == 0:
                # found one more way
                return 1
            if target_remaining < 0 or curr_type >= len(types):
                # this way doesn't fit
                return 0

            sum_ways = 0
            # try to solve [0...COUNTi] questions
            for n_questions in range(types[curr_type][I_COUNT] + 1):
                sum_ways += dfs(curr_type + 1, target_remaining - n_questions * types[curr_type][I_MARK])
            return sum_ways

        result = dfs(0, target)
        return result % mod

    # DP/bottom up: https://leetcode.com/problems/number-of-ways-to-earn-points/solutions/3258120/java-c-python-knapsack-dp/
    def waysToReachTarget(self, target, types):
        dp = [1] + [0] * target
        mod = 10 ** 9 + 7
        for curr_type, curr_mark in types:
            for i in range(target, -1, -1):
                for k in range(1, min(curr_type, i // curr_mark) + 1):
                    dp[i] = (dp[i] + dp[i - curr_mark * k]) % mod
        return dp[-1]