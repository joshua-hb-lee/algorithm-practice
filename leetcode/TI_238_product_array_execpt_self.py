"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
without division

prefix      postfix
[1 2] | 3 | [4 5 6]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        prefix = postfix = 1
        
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer
