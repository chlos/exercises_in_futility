class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        # move right
        for ri in range(n):
            if words[(startIndex + ri) % n] == target:
                break
        else:
            # not found
            return -1
        
        # move left
        for li in range(n):
            if words[(startIndex - li) % n] == target:
                break

        return min(li, ri)