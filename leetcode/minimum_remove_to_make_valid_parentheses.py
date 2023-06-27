class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack_open = []
        i_remove = set()
        for i, ch in enumerate(s):
            if ch not in "()":
                # not a bracket
                continue

            if ch == "(":
                stack_open.append(i)
            elif not stack_open:
                # ')' without a pairing '('; it makes balance negative and cannot be fixed later
                i_remove.add(i)
            else:
                # found a valid '()' pair
                stack_open.pop()
        # remove remainging '(' without a pair
        # i_remove = i_remove.union(set(stack_open))
        i_remove = i_remove.union(stack_open)

        res = []
        for i, ch in enumerate(s):
            if i in i_remove:
                continue
            res.append(ch)

        return "".join(res)
