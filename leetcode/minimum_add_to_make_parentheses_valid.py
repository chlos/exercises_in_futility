class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        add_count = 0
        opening_stack = []
        for ch in s:
            if ch == "(":
                opening_stack.append(ch)
            elif ch == ")":
                if opening_stack:
                    opening_stack.pop()
                else:
                    add_count += 1

        add_count += len(opening_stack)

        return add_count
