WATER = "0"
ISLAND = "1"
VISITED = "-1"


class Solution:
    # DFS
    # time: O(M*N)
    # space: O(M*N)
    def numIslands_DFS(self, grid: List[List[str]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        result = 0

        def out_of_grid(r, c):
            return (r < 0 or r >= nrows) or (c < 0 or c >= ncols)

        def is_island_dfs(r, c):
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
            ]

            if out_of_grid(r, c) or grid[r][c] != ISLAND:
                return False

            grid[r][c] = VISITED
            for dr, dc in directions:
                is_island_dfs(r + dr, c + dc)

            return True

        for r in range(nrows):
            for c in range(ncols):
                is_island = is_island_dfs(r, c)
                if is_island:
                    result += 1

        return result

    # BFS
    # time: O(M*N)
    # space: O(min(M,N)) ; see the https://imgur.com/gallery/M58OKvB
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        result = 0

        def out_of_grid(r, c):
            return (r < 0 or r >= nrows) or (c < 0 or c >= ncols)

        # mark the current island's points as visited
        def bfs(r, c):
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
            ]

            queue = collections.deque()
            queue.append((r, c))
            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    if out_of_grid(new_r, new_c) or grid[new_r][new_c] != ISLAND:
                        continue
                    queue.append((new_r, new_c))
                    grid[new_r][new_c] = VISITED

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == ISLAND:
                    result += 1
                    grid[r][c] = VISITED
                    bfs(r, c)

        return result