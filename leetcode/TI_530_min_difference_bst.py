"""
530. Minimum Absolute Difference in BST

inorder traverse
      5
     / \
    3   7
   / \
  2   4

2 - 3 - 4 - 5 - 7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        if not root:
            return res

        stack = []
        cur = root
        minus = None
        
        # inorder traverse
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            if minus != None:
                res = min(res, abs(minus - cur.val))
                
            minus = cur.val

            cur = cur.right
        
        return res

class Solution2:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDist = [float('inf')]
        prev = [None]
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            
            if prev[0] is not None:
                minDist[0] = min(minDist[0], node.val - prev[0])
            
            prev[0] = node.val
            
            dfs(node.right)
            
        dfs(root)
        return minDist[0]
