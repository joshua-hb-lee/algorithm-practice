"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0 # left, right
        
        while r < len(nums):
            count = 1

            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count = count + 1
                r = r + 1
            
            nums[l] = nums[r]
            l = l + 1
            r = r + 1
        
        return l