"""
169. Majority Element
Boyer-Moore Majority Vote Algorithm
https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
if count is zero, then candidate is updated
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count = count + 1
                continue
            
            if candidate == nums[i]:
                count = count + 1
            
            if candidate != nums[i]:
                count = count - 1
        
        return candidate
