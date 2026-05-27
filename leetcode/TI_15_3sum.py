"""
15. 3Sum

Two pointers
[-1,0,1,2,-1,-4]

sorting > -4 -1 -1 0 1 2
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                b = nums[l]
                c = nums[r]
                cal = a + b + c
                
                if cal > 0:
                    r -= 1
                elif cal < 0:
                    l += 1  
                else:
                    res.append([a, b, c])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
