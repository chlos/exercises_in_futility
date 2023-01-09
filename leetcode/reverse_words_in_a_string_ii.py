def reverseWord(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

        left, right = 0, 0
        while right < len(s):
            if s[right] == ' ':
                reverseWord(s, left, right - 1)
                left = right + 1
            elif right == len(s) - 1:
                reverseWord(s, left, right)
            right += 1