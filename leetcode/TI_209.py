"""
209. Minimum Size Subarray Sum

Two pointers & Sliding window
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, r = 0, 0
        res = len(nums) + 1
        total = nums[l]
        while l < len(nums) and r < len(nums):
            if total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
            else:
                r += 1
                if r < len(nums):
                    total += nums[r]

        if res == len(nums) + 1:
            return 0

        return res
        
# Advanced solution
class Solution2:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res