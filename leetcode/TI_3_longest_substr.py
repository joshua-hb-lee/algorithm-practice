"""
3. Longest Substring Without Repeating Characters

Two pointers & Sliding window (l, r)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # datastructure set is needed to check if the right index character is already in the substring
        # with time complexity O(1)
        check = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            check.add(s[r])

        return res