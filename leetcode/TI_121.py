"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

           [7  2 10  3  1  5]
base    7   7  2  2  2  1  1
cal (first) 0 -5  8  1 -1  4
result  0   0  0  8  8  8  8
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        base, result = prices[0], 0

        for i in range(len(prices)):
            profit = prices[i] - base
            if profit < 0:
                base = prices[i]
            
            if profit > 0 and result < profit:
                result = profit

        return result