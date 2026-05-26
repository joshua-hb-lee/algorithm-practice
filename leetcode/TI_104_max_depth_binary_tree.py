"""
104. Maximum Depth of Binary Tree

DFS (with stack)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        farthest = 0

        if not root:
            return 0

        stack = [[root, 1]]
        while len(stack) != 0:
            target = stack.pop()
            node = target[0]
            depth = target[1]
            if not node.left and not node.right and farthest < depth:
                farthest = depth

            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])

        return farthest
