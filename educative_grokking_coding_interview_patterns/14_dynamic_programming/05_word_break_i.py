class Solution:
    # brute force -> dfs/top down + memo
    def wordBreak_DFS(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def recur(start):
            # base case, scanning is over
            if start >= len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and recur(end):
                    return True

            return False

        return recur(0)

    # bottom up DP
    # https://leetcode.com/problems/word-break/solutions/43808/simple-dp-solution-in-python-with-description/comments/1667513
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] is True if there is a word in wordDict that ends at i-th index of s
        # AND dp is also True at the beginning of the word (dp[i - len(word)])
        dp = [False] * (len(s) + 1)
        dp[0] = True    # empty string always fits

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    if dp[i - len(word)]:
                        dp[i] = True
                        break

        return dp[-1]