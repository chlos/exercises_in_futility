# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/solutions/1646594/left-to-right-and-right-to-left/
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def validate(s, locked, bracket):
            balance = 0
            unlocked = 0
            for i in range(len(s)):
                if locked[i] == "1":
                    if s[i] == bracket:
                        balance += 1
                    else:
                        balance -= 1
                else:
                    unlocked += 1

                if unlocked + balance < 0:
                    return False

            return balance <= unlocked

        return (
            len(s) % 2 == 0
            and validate(s, locked, "(")
            and validate(s[::-1], locked[::-1], ")")
        )
