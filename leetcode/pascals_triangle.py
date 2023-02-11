class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row_idx in range(numRows):
            row = [0] * (row_idx + 1)
            for i in range(len(row)):
                if i == 0 or i == len(row) - 1:
                    row[i] = 1
                else:
                    row[i] = result[row_idx - 1][i - 1] + result[row_idx - 1][i]
            result.append(row)

        return result