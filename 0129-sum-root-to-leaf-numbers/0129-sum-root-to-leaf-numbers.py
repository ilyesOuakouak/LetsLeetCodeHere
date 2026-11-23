# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
  
        def dfs(node, current):
            if not node:
                return 0

            current = current * 10 + node.val
            leaf = node.left is None and node.right is None

            if leaf:
                return current
            
            return dfs(node.left, current) + dfs(node.right, current)
    
        return dfs(root, 0)

            
