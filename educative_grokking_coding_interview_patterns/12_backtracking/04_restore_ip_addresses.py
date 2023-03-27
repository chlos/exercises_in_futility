class Solution:
    def isValid(self, seg: str) -> bool:
        if not seg or len(seg) > 3 or (seg[0] == '0' and len(seg) > 1) or int(seg) > 255:
            return False
        return True

    # iterative
    # https://leetcode.com/problems/restore-ip-addresses/solutions/3079263/leetcode-the-hard-way-explained-line-by-line/
    def restoreIpAddresses_iter(self, s: str) -> List[str]:
        result = []
        if len(s) > 12:
            return result

        # check segments [seg1].[seg2].[seg3].[seg4]
        for i in range(1, 4):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    seg1, seg2, seg3, seg4 = s[:i], s[i:j], s[j:k], s[k:]
                    if all(map(self.isValid, (seg1, seg2, seg3, seg4))):
                        result.append(f'{seg1}.{seg2}.{seg3}.{seg4}')

        return result

    # backtracking
    # https://leetcode.com/problems/restore-ip-addresses/solutions/31140/python-easy-to-understand-solution-backtracking/
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if len(s) > 12:
            return result

        def backtrack(s_suffix, seg_no, curr_result):
            if seg_no > 4:
                return
            # we have 4 valid segments and we reached the end of the string
            if seg_no == 4 and not s_suffix:
                result.append(curr_result[:-1]) # [:-1] strips the "extra" dot in the end
                return

            # try different options for the current segment
            for i in range(1, len(s_suffix) + 1):
                seg = s_suffix[:i]
                if self.isValid(seg):
                    backtrack(s_suffix[i:], seg_no + 1, curr_result + seg + '.')

        backtrack(s, 0, '')
        return result