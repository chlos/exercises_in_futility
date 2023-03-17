class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # not enough gas, no solution
        if sum(gas) - sum(cost) < 0:
            return -1

        total_gas = 0
        start_idx = 0
        for curr_idx in range(len(gas)):
            total_gas += gas[curr_idx] - cost[curr_idx]
            if total_gas < 0:
                # it was wrong starting point
                start_idx = curr_idx + 1
                total_gas = 0

        return start_idx