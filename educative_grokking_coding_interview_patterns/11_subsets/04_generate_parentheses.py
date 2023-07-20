BRACKET_OPEN = '('
BRACKET_CLOSE = ')'


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(n, count_open, count_close, curr_brackets, result):
            if count_open >= n and count_close >= n:
                result.append(''.join(curr_brackets))
                return

            if count_open < n:
                curr_brackets.append(BRACKET_OPEN)
                backtrack(n, count_open + 1, count_close, curr_brackets, result)
                curr_brackets.pop()

            if count_close < count_open:
                curr_brackets.append(BRACKET_CLOSE)
                backtrack(n, count_open, count_close + 1, curr_brackets, result)
                curr_brackets.pop()

        result = []
        backtrack(n, 0, 0, [], result)

        return result