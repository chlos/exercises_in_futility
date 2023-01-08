MAX_REPLACEMENTS = 2


class Solution:
    def makePalindrome(self, s: str) -> bool:
        replacements = 0
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if replacements >= MAX_REPLACEMENTS:
                    return False
                replacements += 1

            left += 1
            right -= 1

        return True