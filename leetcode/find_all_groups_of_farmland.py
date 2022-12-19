class Solution:
    # DFS: https://leetcode.com/problems/find-all-groups-of-farmland/solutions/1640116/python3-dfs-easy-to-understand/
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        nrows = len(land)
        ncols = len(land[0])
        directions = [
            # r, c
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        def dfs(r, c):
            if (r < 0 or r >= nrows) or (c < 0 or c >= ncols) or land[r][c] == 0:
                return [0, 0]

            # mark as visited
            land[r][c] = 0

            bottom_right = [r, c]
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                new_bottom_right = dfs(new_r, new_c)
                bottom_right[0] = max(bottom_right[0], new_bottom_right[0])
                bottom_right[1] = max(bottom_right[1], new_bottom_right[1])

            return bottom_right

        res = []
        for r in range(nrows):
            for c in range(ncols):
                if land[r][c] == 0:
                    continue
                bottom_right = dfs(r, c)
                # add [r1, c1, r2, c2]
                res.append([r, c] + bottom_right)

        return res