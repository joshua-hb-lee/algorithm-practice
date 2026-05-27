"""
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

0 0 1 1 1 1 2 2 2 3 3
  l       r
count=4
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count = count + 1
                r = r + 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l = l + 1

            r = r + 1

        return l
