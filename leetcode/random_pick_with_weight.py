class Solution:

    def __init__(self, w: List[int]):
        self.running_sums = [0 for _ in range(len(w))]
        self.running_sums[0] = w[0]
        for i in range(1, len(w)):
            self.running_sums[i] = self.running_sums[i - 1] + w[i]

    def pickIndex(self) -> int:
        random_num = random.random() * self.running_sums[-1]

        left = 0
        right = len(self.running_sums)
        while left < right:
            mid = (left + right) // 2

            if self.running_sums[mid] < random_num:
                left = mid + 1
            else:
                right = mid

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()