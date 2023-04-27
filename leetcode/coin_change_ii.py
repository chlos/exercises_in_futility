class Solution:
    # top down / dfs + memo/cache
    def change_DFS(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(coin_i, amount):
            # success, +1 combination
            if amount == 0:
                return 1
            # failed
            if amount < 0 or coin_i >= len(coins):
                return 0

            return (
                dfs(coin_i, amount - coins[coin_i]) +
                dfs(coin_i + 1, amount)
            )

        coins.sort(reverse=True)    # speed up
        return dfs(0,amount)

    # bottom up dp
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for curr_amount in range(coin, amount + 1):
                dp[curr_amount] += dp[curr_amount - coin]

        if dp[-1] == float('inf'):
            return 0
        return dp[-1]