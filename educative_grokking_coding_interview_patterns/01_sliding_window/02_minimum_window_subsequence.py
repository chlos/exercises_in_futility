class Solution:
    def minWindow(self, str1: str, str2: str) -> str:
        min_len = float('inf')
        min_subseq = ''
    
        idx_s1, idx_s2 = 0, 0
        while idx_s1 < len(str1):
            print('...', idx_s1, idx_s2)
            if str1[idx_s1] == str2[idx_s2]:
                idx_s2 += 1
                if idx_s2 == len(str2):
                    # we met the full subseq
                    # decrement idx_s2 and start reverse loop
                    print('met full sub at idx_s1, idx_s2:', idx_s1, idx_s2)
                    start, end = idx_s1, idx_s1
                    idx_s2 -= 1
                    while idx_s2 >= 0:
                        # move idx_s2 left to check all str2 chars
                        if str1[start] == str2[idx_s2]:
                            print(str1[start])
                            idx_s2 -= 1
                        # move start left
                        start -= 1
                        print('start:', start, 'idx_s2:', idx_s2)
                    # move start right to the subseq start position
                    start += 1

                    curr_len = end - start + 1
                    if curr_len < min_len:
                        min_len = curr_len
                        print(start, end)
                        min_subseq = str1[start:end + 1]

                    # we will continue checking from the next char to the first seq's char
                    # str1: abcdefgh; str2: bdf; subseq: a(bcdef)gh
                    # we'll continue with: ...CBDEFGH
                    idx_s1 = start
                    idx_s2 = 0

            idx_s1 += 1
    
        return min_subseq