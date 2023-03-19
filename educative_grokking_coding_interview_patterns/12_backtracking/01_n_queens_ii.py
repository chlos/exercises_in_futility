class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(curr_row, diags, anti_diags, cols):
            # all queens are safe, good combination found!
            if curr_row >= n:
                return 1

            # traverse posible solutions
            solutions = 0
            for curr_col in range(n):
                curr_diag = curr_row - curr_col
                curr_anti_diag = curr_row + curr_col
                # queen is in danger at this column
                if (
                    curr_col in cols or
                    curr_diag in diags or
                    curr_anti_diag in anti_diags
                ):
                    continue

                # try to place current queen on this row and col
                diags.add(curr_diag)
                anti_diags.add(curr_anti_diag)
                cols.add(curr_col)

                # go deeper
                solutions += backtrack(curr_row + 1, diags, anti_diags, cols)

                # remove the current queen, bc we are backtracking from this solutions subtree
                diags.remove(curr_diag)
                anti_diags.remove(curr_anti_diag)
                cols.remove(curr_col)

            return solutions

        # start with a first row
        return backtrack(0, set(), set(), set())