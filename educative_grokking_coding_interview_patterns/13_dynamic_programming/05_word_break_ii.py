class Solution:
    # dfs / top-down
    # see the: https://leetcode.com/problems/word-break-ii/solutions/44311/python-easy-to-understand-solution/comments/881748
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # a bit faster in 'word in wordDict' checks
        # wordDict = set(wordDict)
        wordDict = {w: True for w in wordDict}

        result = []

        def dfs(start, path):
            if start >= len(s):
                result.append(' '.join(path))

            for end in range(start + 1, len(s) + 1):
                curr_word = s[start:end]
                if curr_word in wordDict:
                    dfs(end, path + [curr_word])

        dfs(0, [])
        return result