class Solution:
    # sliding window; dict + string slices for calculating hashes
    def findRepeatedDnaSequences_windowDict(self, s: str) -> List[str]:
        k = 10
        if len(s) < k:
            return []

        seq_set = set()
        seq_hashes = collections.defaultdict(int)
    
        for i in range(len(s) - k + 1):
            seq = s[i:i + k]
            seq_hashes[seq] += 1
            if seq_hashes[seq] > 1:
                seq_set.add(seq)
    
        return seq_set

    # sliding window; rollling hash
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        if len(s) < k:
            return []

        seq_set = set()
        hash_set = set()

        # convert string to ints (to count hashes)
        mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        numbers = []
        for ch in s:
            numbers.append(mapping[ch])
        # constant a=4 because we have only 4 nucleotides
        base = 4
        # a^k, the highest place value
        hi = pow(base, k)
    
        hash = 0
        for i_start in range(len(s) - k + 1):
            # caclulate the rolling hash
            if i_start > 0:
                # increase the place value of each element by factor base
                hash = hash * base                        
                # subtract the hash of the outgoing nucleotide
                hash -= numbers[i_start - 1] * hi
                # add the hash of the incoming nucleotide
                hash += numbers[i_start + k - 1]     
            else:
                # calculating the hash for the first window
                for i_end in range(k):              
                    # accumulate the hash values
                    hash = hash * base + numbers[i_end] 

            # check if it's repeated sea
            if hash in hash_set:
                seq_set.add(s[i_start:i_start + k])
            hash_set.add(hash)

        return seq_set