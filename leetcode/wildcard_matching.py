def prune_pattern(p):
    new_pattern = []
    for ch in p:
        if not new_pattern or ch != '*':
            new_pattern.append(ch)
        elif new_pattern[-1] != '*':
            new_pattern.append(ch)
    return ''.join(new_pattern)


# DFS with Memoization
# https://leetcode.com/problems/wildcard-matching/solutions/1336621/python-dfs-with-memoization-clean-concise/
class Solution_DFS:
    def isMatch(self, s: str, p: str) -> bool:
        # https://stackoverflow.com/questions/49883177/how-does-lru-cache-from-functools-work
        @lru_cache(None)
        def dfs(si, pi):
            # Reach full pattern
            if pi == len(p):
                # Reach full string
                return si == len(s)

            # Match Single character
            if si < len(s) and (s[si] == p[pi] or p[pi] == '?'):
                return dfs(si + 1, pi + 1)

            # Match zero or one or more character
            if p[pi] == '*':
                return dfs(si, pi + 1) or si < len(s) and dfs(si + 1, pi)

            return False

        p = prune_pattern(p)
        return dfs(0, 0)


# backtracking
# https://leetcode.com/problems/wildcard-matching/solutions/294659/wildcard-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = prune_pattern(p)

        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1

            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1

            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif star_idx == -1:
                return False

            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        # The remaining characters in the pattern should all be '*' characters
        return all(p[i] == '*' for i in range(p_idx, p_len))