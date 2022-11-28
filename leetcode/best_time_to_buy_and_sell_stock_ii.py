import collections
from typing import List


class Solution:
    # monotonic growing deque/stack
    def maxProfit_monotonicStack(self, prices: List[int]) -> int:
        max_profit = 0
        mono = collections.deque()

        for price in prices:
            if not mono:
                mono.append(price)
                continue

            # we found a new local min
            # let's count local profit for a previous [min_price...max_price] interval
            # then clear the stack
            if price < mono[-1]:
                max_profit += mono[-1] - mono[0]
                while mono:
                    mono.pop()

            mono.append(price)

        # don't forget about the last segment
        if mono:
            max_profit += mono[-1] - mono[0]

        return max_profit

    # sum of diffs in each segment
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                max_profit += curr_profit
                curr_profit = 0
            else:
                curr_profit += prices[i] - prices[i - 1]
        max_profit += curr_profit

        return max_profit