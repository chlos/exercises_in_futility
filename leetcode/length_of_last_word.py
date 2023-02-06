class Solution:
    # brute-force O(N): iterate through the whole string from the beginning
    def lengthOfLastWord_brute(self, s: str) -> int:
        count = 0
        curr_count = 0
        for ch in s:
            if ch.isspace():
                if curr_count > 0:
                    count = curr_count
                curr_count = 0
            else:
                curr_count += 1
        if curr_count > 0:
            count = curr_count

        return count

    # backward iterating O(N)
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s)
        while i > 0:
            i -= 1
            # in the middle of the last word
            if not s[i].isspace():
                count += 1
            # last word ended
            elif count > 0:
                return count

        return count