class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort by (costA - costB) difference
        costs.sort(key=lambda c: c[0] - c[1])

        total = 0
        n = len(costs) // 2
        for i in range(n):
            # first half goes to A (because it's cheaper due to A-B diff)
            # second half goes to B
            total += costs[i][0] + costs[i + n][1]

        return total