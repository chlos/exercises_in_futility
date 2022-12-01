class Solution:
    # time: n
    # space: n
    def sortedSquares_1(self, nums: List[int]) -> List[int]:
        sorted_squares = []
        negative_squares = []
        for n in nums:
            sq = n ** 2
            if n < 0:
                negative_squares.append(sq)
            else:
                while negative_squares and negative_squares[-1] < sq:
                    sorted_squares.append(negative_squares.pop())
                sorted_squares.append(sq)

        while negative_squares:
            sorted_squares.append(negative_squares.pop())

        return sorted_squares

    # time: n
    # space: 1
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_squares = [0] * len(nums)

        li = 0
        ri = len(nums) - 1
        for i in reversed(range(len(nums))):
            if abs(nums[li]) < abs(nums[ri]):
                n = nums[ri]
                ri -= 1
            else:
                n = nums[li]
                li += 1
            sorted_squares[i] = n ** 2

        return sorted_squares