"""
274. H-Index

https://en.wikipedia.org/wiki/H-index
The maximun number value of *h* (>= h papers, >= h citations)

10, 8, 5, 4, 3 >> h=4
"""
from typing import List

# can think about converting into citation index array [paper_cite_counts]
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_cite_counts = [0] * (n + 1) # to include 0 citation

        for i in range(n):
            paper_cite_counts[min(n, citations[i])] += 1

        h = n
        papers = paper_cite_counts[n]
        while papers < h:
            h -= 1
            papers += paper_cite_counts[h]

        return h
