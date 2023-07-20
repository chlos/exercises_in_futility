VISITED = '*'
DIRECTIONS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]


class Solution_VisitedSets:
    # no input editing (good for the interview and for the production code!)
    # but it timeouts :(
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        if rows * cols < len(word):
            return False

        def out_of_grid(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return True
            return False

        def backtrack(row, col, curr_i, visited):
            # wrong letter, let's go back
            if board[row][col] != word[curr_i]:
                return False

            # word found
            if curr_i == len(word) - 1:
                return True

            # let's go deeper
            for drow, dcol in DIRECTIONS:
                # skip invalid and visited
                new_row, new_col = row + drow, col + dcol
                if out_of_grid(new_row, new_col) or (new_row, new_col) in visited:
                    continue

                visited.add((new_row, new_col))
                if backtrack(new_row, new_col, curr_i + 1, visited) == True:
                    return True
                visited.remove((new_row, new_col))

            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0, {(row, col)}) == True:
                    return True

        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        if rows * cols < len(word):
            return False

        def out_of_grid(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return True
            return False

        def backtrack(row, col, suffix):
            # word found
            if len(suffix) == 0:
                return True

            # invalid place or wrong letter, let's go back
            if out_of_grid(row, col) or board[row][col] != suffix[0]:
                return False

            # mark as visited
            board[row][col] = VISITED
            # let's go deeper
            for drow, dcol in DIRECTIONS:
                if backtrack(row + drow, col + dcol, suffix[1:]) == True:
                    return True
            # mark as visited
            board[row][col] = suffix[0]

            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, word) == True:
                    return True

        return False
