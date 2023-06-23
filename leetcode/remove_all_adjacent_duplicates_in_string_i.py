class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for ch in s:
            if len(res) > 0 and res[-1] == ch:
                res.pop()
                continue
            res.append(ch)

        return "".join(res)
