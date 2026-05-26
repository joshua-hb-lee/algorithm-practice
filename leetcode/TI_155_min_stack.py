"""
155. Min Stack

https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150

- Double Stack
stack: [2, -5, 10, -3, 2, -15, 20]
minIdxStack: [0, 1, 5]
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minIdxStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minIdxStack) == 0:
            self.minIdxStack.append(0)
            return

        if self.stack[self.minIdxStack[-1]] >= val:
            self.minIdxStack.append(len(self.stack) - 1)

    def pop(self) -> None:
        # when min value is the target to be popped
        if self.minIdxStack[-1] == len(self.stack) - 1:
            self.minIdxStack.pop()

        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]       
        
    def getMin(self) -> int:
        return self.stack[self.minIdxStack[-1]]
        