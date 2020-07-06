#!/usr/bin/env python3


class Solution:
    def reverseWords_naive(self, s: str) -> str:
        return ' '.join((word[::-1] for word in s.split()))

    def reverseWords(self, s: str) -> str:
        s_chars = list(s)
        l, r = 0, 0
        while r < len(s):
            if s_chars[r].isspace() or r == len(s) - 1:
                if r == len(s) - 1:
                    r += 1
                for i in range((r - l) // 2):
                    s_chars[l + i], s_chars[r - i - 1] = s_chars[r - i - 1], s_chars[l + i]
                l, r = r + 1, r + 1
                continue
            r += 1

        return ''.join(s_chars)


if __name__ == "__main__":
    s = Solution()

    str_in = "Let's take LeetCode contest"
    str_expected = "s'teL ekat edoCteeL tsetnoc"
    str_out = s.reverseWords(str_in)
    print('expected "{}"\nactual "{}"'.format(str_expected, str_out))
    assert str_out == str_expected
    print('OK')