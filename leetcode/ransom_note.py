class Solution:
    # two hashmaps
    def canConstruct_twoHashMaps(self, ransomNote: str, magazine: str) -> bool:
        note_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)
        for letter in note_count:
            if note_count[letter] > magazine_count[letter]:
                return False
        return True

    # one hashmap
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count= collections.Counter(magazine)
        for letter in ransomNote:
            curr_mag_count = magazine_count[letter]
            if curr_mag_count <= 0:
                return False
            magazine_count[letter] -= 1

        return True