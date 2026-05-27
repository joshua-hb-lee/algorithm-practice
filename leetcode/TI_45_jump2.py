"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

using BFS
[2, 3, 1, 1, 4]
(2) -> (3, 1) -> (1, 4)
need farthest index from each layer
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            
            res += 1
            l = r + 1
            r = farthest
            
        return res