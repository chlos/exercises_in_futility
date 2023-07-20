class Solution:
    # top down / dfs / backtracking
    def climbStairs_dfs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1

            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1   # 1 way: 1
        dp[2] = 2   # 2 ways: 1+1 or 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[-1]