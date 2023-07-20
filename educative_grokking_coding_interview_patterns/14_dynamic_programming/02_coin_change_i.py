class Solution:
    # top down/dfs + memo/caching
    # https://leetcode.com/problems/coin-change/solutions/1371738/c-recursion-dp-memoization-dp-tabulation/
    def coinChange_DFSCache(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(coin_i, amount_remaining):
            # base cases
            if amount_remaining < 0 or coin_i >= len(coins):
                # impossible to get "amount" using this subset of coins
                return float('inf')
            if amount_remaining == 0:
                # we found one of the subsets of coins to get "amount"
                return 0

            take_coin = float('inf')
            # take this coin and try to take it one more time
            if coins[coin_i] <= amount_remaining:
                take_coin = 1 + dfs(coin_i, amount_remaining - coins[coin_i])
            # skip this coin; it's time to move on with a next coin
            dont_take_coin = 0 + dfs(coin_i + 1, amount_remaining)

            return min(take_coin, dont_take_coin)

        result = dfs(0, amount)
        if result < float('inf'):
            return result
        else:
            return -1

    # top down/dfs + memo/manual
    # https://leetcode.com/problems/coin-change/solutions/1371738/c-recursion-dp-memoization-dp-tabulation/
    def coinChange_DFSMemo(self, coins: List[int], amount: int) -> int:
        # memo[coin_i][amount_remaining]
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(coin_i, amount_remaining):
            # base cases
            if amount_remaining < 0 or coin_i >= len(coins):
                # impossible to get "amount" using this subset of coins
                return float('inf')
            if amount_remaining == 0:
                # we found one of the subsets of coins to get "amount"
                return 0

            if memo[coin_i][amount_remaining] != -1:
                return memo[coin_i][amount_remaining]

            take_coin = float('inf')
            # take this coin and try to take it one more time
            if coins[coin_i] <= amount_remaining:
                take_coin = 1 + dfs(coin_i, amount_remaining - coins[coin_i])
            # skip this coin; it's time to move on with a next coin
            dont_take_coin = 0 + dfs(coin_i + 1, amount_remaining)

            memo[coin_i][amount_remaining] = min(take_coin, dont_take_coin)
            return memo[coin_i][amount_remaining]

        result = dfs(0, amount)
        if result < float('inf'):
            return result
        else:
            return -1

    # bottom up DP
    # https://leetcode.com/problems/coin-change/solutions/778548/c-dp-solution-explained-100-time-100-space/
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for curr_coin in coins:
            for curr_amount in range(curr_coin, amount + 1):
                dp[curr_amount] = min(
                    dp[curr_amount],
                    1 + dp[curr_amount - curr_coin]
                )

        result = dp[amount]
        if result < float('inf'):
            return result
        else:
            return -1