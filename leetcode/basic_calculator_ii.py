class Solution:
    # stack
    def calculate_stack(self, s: str) -> int:
        def upd(operator, operand):
            if operator == "+":
                stack.append(operand)
            elif operator == "-":
                stack.append(-operand)
            elif operator == "*":
                stack.append(stack.pop() * operand)
            elif operator == "/":
                stack.append(int(stack.pop() / operand))

        operand = 0
        prev_operator = "+"
        res = 0

        stack = []
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)

            elif ch in "+-*/":
                upd(prev_operator, operand)
                operand = 0
                prev_operator = ch

        upd(prev_operator, operand)
        return sum(stack)

    def calculate(self, s):
        res = 0
        operand, tmp_res, prev_operator = 0, 0, "+"

        # add "##" to dump the last operator
        for ch in s + "##":
            if ch == " ":
                continue
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            else:
                if prev_operator == "*":
                    tmp_res *= operand
                elif prev_operator == "/":
                    tmp_res = int(tmp_res / operand)
                else:
                    res += tmp_res
                    tmp_res = operand if prev_operator == "+" else -operand
                prev_operator, operand = ch, 0
        return res
