"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150

BFS and queue
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        queue = [[root, 0]]
        leftIdx = 0
        level = 0

        while leftIdx < len(queue):
            target = queue[leftIdx]
            node = target[0]
            level = target[1]

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
            
            leftIdx += 1
            if leftIdx >= len(queue) or level != queue[leftIdx][1]:
                res.append(node.val)

        return res
