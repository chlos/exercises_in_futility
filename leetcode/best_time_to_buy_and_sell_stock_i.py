#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


class Solution:
    # keep track min
    # time O(n)
    # space O(1)
    def maxProfit(self, prices: List[int]) -> int:
        min_price_i = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_price_i]:
                min_price_i = i
            else:
                curr_profit = prices[i] - prices[min_price_i]
                max_profit = max(max_profit, curr_profit)

        return max_profit