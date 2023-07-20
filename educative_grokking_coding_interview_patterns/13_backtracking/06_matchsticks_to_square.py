class Solution:
    # DFS + Memoization
    #
    # Not too effective because of repeating permutations:
    # Why permutations?
    # Even though in the real world we don't care about the order of these sides as they all have to be equal in the end, for caching purposes, the order does matter.
    # A cache entry (1,1,4,1) is different to the entry (1,4,1,1). So, the drawback of this solution is that we're doing more work than it's actually required.
    #
    # https://leetcode.com/problems/matchsticks-to-square/solutions/2270337/python3-dfs-cache-easy-to-understand/
    # https://leetcode.com/problems/matchsticks-to-square/solutions/2274058/python-from-dfs-to-optimized-dp-using-bitmasks/
    def makesquare(self, matchsticks: List[int]) -> bool:
        if (
            len(matchsticks) < 4 or
            sum(matchsticks) < 4 or
            sum(matchsticks) % 4 != 0
        ):
            return False

        matchsticks.sort(reverse=True)

        side_len = sum(matchsticks) // 4

        @cache
        def backtrack(curr_match_i, len_1, len_2, len_3, len_4):
            if len_1 == len_2 == len_3 == len_4 == side_len:
                return True

            if curr_match_i > len(matchsticks) - 1:
                return False
            if len_1 > side_len or len_2 > side_len or len_3 > side_len or len_4 > side_len:
                return False

            return (
                backtrack(curr_match_i + 1, len_1 + matchsticks[curr_match_i], len_2, len_3, len_4) or
                backtrack(curr_match_i + 1, len_1, len_2 + matchsticks[curr_match_i], len_3, len_4) or
                backtrack(curr_match_i + 1, len_1, len_2, len_3 + matchsticks[curr_match_i], len_4) or
                backtrack(curr_match_i + 1, len_1, len_2, len_3, len_4 + matchsticks[curr_match_i])
            )

        return backtrack(0, 0, 0, 0, 0)