# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            return 1 + max(left, right)

        
        return dfs(root)
       


































"""
def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        maxi = max(left, right) + 1
        print(['node', root.val, 'left', left, 'right', right, 'max', maxi])


        return max(left, right) + 1
"""