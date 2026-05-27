"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

They have 3 methods to resolve
"""
from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)
# not recommended
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]

"""
[1, 2, 3, 4, 5, 6, 7]
→ [7, 6, 5, 4, 3, 2, 1] (0, size - 1)
→ [5, 6, 7, 4, 3, 2, 1] (0, k - 1)
→ [5, 6, 7, 1, 2, 3, 4] (k, size - 1)
"""
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, size - 1)
        reverse(0, k - 1)
        reverse(k, size - 1)