"""
55. Jump Game

DP & Greedy
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
"""


from typing import List

# DP - very inefficient
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            farthest = nums[i] + i
            if farthest >= n - 1:
                dp[i] = True
                continue

            for j in range(i + 1, farthest + 1):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]

# Greedy
# starting at the last position, and moving backward
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        result = False
        
        for i in range(len(nums) - 1, -1, -1):
            result = nums[i] >= distance
            distance = 1 if result else distance + 1
        
        return result
   
# Greedy advanced 
class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i
        
        return True if target == 0 else False