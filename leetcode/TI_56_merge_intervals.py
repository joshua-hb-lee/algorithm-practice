"""
56. Merge Intervals
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]

        for i in range(0, len(intervals)):
            latest = res[-1]
            if latest[1] >= intervals[i][0]:
                latest[0], latest[1] = latest[0], max(latest[1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res

# advanced
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])

        return res
        