"""
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

map: {10: 2, 20: 0, 30: 1, 40: 3}
list: [20, 30, 10, 40]

remove 30
[20, _, 10, 40]
[20, 40, 10]
{10: 2, 20: 0, 30: 1, 40: 3} -> {10: 2, 20: 0, 40: 1}
"""

import random


class RandomizedSet:
    def __init__(self):
        self.numDict = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        not_exists = val not in self.numDict
        
        if not_exists:
            self.numDict[val] = len(self.numList)
            self.numList.append(val)

        return not_exists

    def remove(self, val: int) -> bool:
        exists = val in self.numDict

        if exists:
            idx = self.numDict[val]
            last_value = self.numList[-1]
            self.numList[idx] = last_value
            self.numDict[last_value] = idx
            del self.numDict[val]
            del self.numList[-1]

        return exists

    def getRandom(self) -> int:
        return random.choice(self.numList)
