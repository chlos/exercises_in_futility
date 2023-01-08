def isPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


class Solution:
    # my clumsy solution
    def validPalindrome_my(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:

                orig_left, orig_right = left, right
                left += 1
                ok = True
                while left < right:
                    if s[left] != s[right]:
                        ok = False
                        break
                    left += 1
                    right -= 1
                if ok:
                    return True

                left, right = orig_left, orig_right
                right -= 1
                while left < right:
                    if s[left] != s[right]:
                        return False
                    left += 1
                    right -= 1

            left += 1
            right -= 1

        return True

    # clean solution
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1)
            
            left += 1
            right -= 1

        return True