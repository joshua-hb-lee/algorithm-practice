"""
122. Best Time to Buy and Sell Stock II

think about a fluctuating graph
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pick, result, best = prices[0], 0, 0

        for i in range(len(prices)):
            profit = prices[i] - pick

            # downward
            if i > 0 and prices[i] < prices[i - 1]:
                pick = prices[i]
                best = 0
                continue
            
            # upward and choose the best profit
            if profit > 0:
                result += profit
                if best <= profit:
                    result -= best
                    best = profit
            
        return result
