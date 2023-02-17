class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if (
            (s == t) or
            (abs(len(s) - len(t)) > 1)
        ):
            return False

        edit_count = 0
        s_idx, t_idx = 0, 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] != t[t_idx]:
                edit_count += 1
                if edit_count > 1:
                    return False

                # c(t) vs c(a)t -> c(t) vs ca(t) in next iter
                if len(s) > len(t):
                    t_idx -= 1
                elif len(s) < len(t):
                    s_idx -= 1

            s_idx += 1
            t_idx += 1

        return True