# inspired by: https://leetcode.com/problems/sudoku-solver/solutions/1947604/python-easiest-recursive-solution/
class Solution:
    def printDebug(self, board):
        print('board')
        for r in board:
            print(r)
        print('rows')
        for i in range(9):
            print(f'{i}: {sorted(self.rows[i])}')
        print('cols')
        for i in range(9):
            print(f'{i}: {sorted(self.cols[i])}')
        print('boxes')
        for i in range(9):
            print(f'{i}: {sorted(self.boxes[i])}')

    def getBoxNum(self, row, col):
        '''
        box numbers:
        0 1 2
        3 4 5
        6 7 8
        '''
        return (row // 3) * 3 + (col // 3)

    def calcState(self, board):
        self.rows = collections.defaultdict(set)
        self.cols = collections.defaultdict(set)
        self.boxes = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                curr_num = board[row][col]
                box = self.getBoxNum(row, col)
                if curr_num != '.':
                    self.rows[row].add(curr_num)
                    self.cols[col].add(curr_num)
                    self.boxes[box].add(curr_num)

    def updStateAdd(self, board, row, col, box, num):
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.boxes[box].add(num)

    def updStateRm(self, board, row, col, box, num):
        self.rows[row].discard(num)
        self.cols[col].discard(num)
        self.boxes[box].discard(num)

    def isValid(self, row, col, box, num):
        return (
            num not in self.rows[row] and
            num not in self.cols[col] and
            num not in self.boxes[box]
        )

    def backtrack(self, board, row, col):
        # we've done! all rows processed previously
        if row == len(board):
            return True
        # let's proceed with the next row
        if col == len(board):
            return self.backtrack(board, row + 1, 0)

        # already filled, go to the next cell in the row
        if board[row][col] != '.':
            return self.backtrack(board, row, col + 1)

        # fill the empty cell
        for i in range(1, 10):
            box = self.getBoxNum(row, col)
            if not self.isValid(row, col, box, str(i)):
                continue

            board[row][col] = str(i)
            self.updStateAdd(board, row, col, box, str(i))
            if self.backtrack(board, row, col + 1):
                return True
            # restore the state
            else:
                self.updStateRm(board, row, col, box, str(i))
                board[row][col] = '.'

        # backtrack
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.calcState(board)

        # self.printDebug(board)

        self.backtrack(board, 0, 0)


# don't maintain sets (add/rm) but check the row/col/box "manually" every time
# slower actually
class Solution_noSets:
    def getBoxNum(self, row, col):
        '''
        box numbers:
        0 1 2
        3 4 5
        6 7 8
        '''
        return (row // 3) * 3 + (col // 3)

    def isValid(self, board, row, col, num):
        for i in range(9):
            if board[i][col] == num:
                return False
            if board[row][i] == num:
                return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == num:
                return False

        return True

    def backtrack(self, board, row, col):
        # we've done! all rows processed previously
        if row == len(board):
            return True
        # let's proceed with the next row
        if col == len(board):
            return self.backtrack(board, row + 1, 0)

        # fill the empty cell
        if board[row][col] == '.':
            for i in range(1, 10):
                box = self.getBoxNum(row, col)
                if not self.isValid(board, row, col, str(i)):
                    continue

                board[row][col] = str(i)
                if self.backtrack(board, row, col + 1):
                    return True
                # restore the state
                else:
                    board[row][col] = '.'

            # backtrack
            return False

        # already filled, go to the next cell in the row
        else:
            return self.backtrack(board, row, col + 1)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)