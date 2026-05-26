"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, (start, end) in enumerate(intervals):
            newStart = newInterval[0]
            newEnd = newInterval[1]

            # (1, 2) < new: (3, 4)
            if end < newStart:
                res.append([start, end])
                if i == len(intervals) - 1:
                    res.append(newInterval)
                continue

            # new: (3, 4) < (6, 7)
            if newEnd < start:
                # (3, 4) is first || [(1, 2)] < new: (3, 4)
                if len(res) == 0 or res[-1][1] < newStart:
                    res.append(newInterval)

                res.append([start, end])
                continue
            
            # the lastEnd in res
            # [(1, 2), (3, 8)] < (6, 7) | new: (4, 8)
            if len(res) != 0 and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                # when first appending the new overlapped interval
                # [(1, 2)] < (3, 8) ((3, 5) & new (4, 8))
                res.append([min(newStart, start), max(end, newEnd)])
            
        return res if len(intervals) != 0 else [newInterval]