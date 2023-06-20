class Solution:
    def calculate(self, s: str) -> int:
        operand = 0
        sign = 1
        res = 0

        stack = []
        for ch in s:
            if ch.isdigit():
                # forming operand
                operand = operand * 10 + int(ch)

            elif ch in "+-":
                # evaluate exp on the left
                res += sign * operand
                operand = 0
                # update the new current sign, reset operand
                if ch == "+":
                    sign = 1
                else:
                    sign = -1

            elif ch == "(":
                # save the current progres on the stack
                stack.append(res)
                stack.append(sign)
                # start a fresh as if we are calculating a new expression
                sign = 1
                res = 0

            elif ch == ")":
                # eval exp on the left
                res += sign * operand
                operand = 0
                # apply sign from stack
                res *= stack.pop()
                # add result from stack
                res += stack.pop()

        # dump remaining operand
        return res + sign * operand
