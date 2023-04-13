# knapsack problem
# https://leetcode.com/discuss/study-guide/1152328/01-Knapsack-Problem-and-Dynamic-Programming
# https://leetcode.com/discuss/study-guide/1308617/Dynamic-Programming-Patterns

# great exlanation:
# https://leetcode.com/problems/ones-and-zeroes/solutions/814077/dedicated-to-beginners/
class Solution:
    def countOnesZeros(self, strs):
        count = {}
        for i, curr_str in enumerate(strs):
            ones, zeros = 0, 0
            for val in curr_str:
                if val == '1':
                    ones += 1
                elif val == '0':
                    zeros += 1
            count[i] = (ones, zeros)

        return count

    # dfs recursive top down; timout without memo/caching; let's use python's caching
    def findMaxForm_DFSCache(self, strs: List[str], m: int, n: int) -> int:
        ones_zeros = self.countOnesZeros(strs)

        @lru_cache(maxsize=None)
        def recur(i, ones_left, zeros_left):
            # base cases: no more strs; no more ones and zeros left
            if i >= len(strs) or (ones_left <= 0 and zeros_left <= 0):
                return 0

            curr_ones, curr_zeros = ones_zeros[i]

            # the current str doesn't fit ones/zeros left restriction - skip it and move on
            if curr_ones > ones_left or curr_zeros > zeros_left:
                return recur(i + 1, ones_left, zeros_left)

            return max(
                # take this str to the subset (and increment the subsets counter)
                1 + recur(i + 1, ones_left - curr_ones, zeros_left - curr_zeros),
                # don't take this str
                recur(i + 1, ones_left, zeros_left),
            )

        return recur(0, n, m)

    # dfs recursive top down; memoization implementation
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ones_zeros = self.countOnesZeros(strs)
        dp = [collections.defaultdict(lambda: -1) for _ in range(len(strs))]

        def recur(i, ones_left, zeros_left):
            # base cases: no more strs; no more ones and zeros left
            if i >= len(strs) or (ones_left <= 0 and zeros_left <= 0):
                return 0

            curr_ones, curr_zeros = ones_zeros[i]

            # take the result from cache if any is available
            if dp[i][(ones_left, zeros_left)] > -1:
                return dp[i][(ones_left, zeros_left)]

            # the current str doesn't fit ones/zeros left restriction - skip it and move on
            if curr_ones > ones_left or curr_zeros > zeros_left:
                curr_result = recur(i + 1, ones_left, zeros_left)
                dp[i][(ones_left, zeros_left)] = curr_result
                return curr_result

            curr_result = max(
                # take this str to the subset (and increment the subsets counter)
                1 + recur(i + 1, ones_left - curr_ones, zeros_left - curr_zeros),
                # don't take this str
                recur(i + 1, ones_left, zeros_left),
            )
            dp[i][(ones_left, zeros_left)] = curr_result
            return curr_result

        return recur(0, n, m)

    # DP; bottom up
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ones_zeros = self.countOnesZeros(strs)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(len(strs)):
            curr_ones, curr_zeros = ones_zeros[i]
            for ones_j in range(n, curr_ones-1, -1):
                for zeros_k in range(m, curr_zeros-1, -1):
                    dp[zeros_k][ones_j] = max(
                        dp[zeros_k][ones_j],
                        1 + dp[zeros_k - curr_zeros][ones_j - curr_ones]
                    )

        return dp[m][n]