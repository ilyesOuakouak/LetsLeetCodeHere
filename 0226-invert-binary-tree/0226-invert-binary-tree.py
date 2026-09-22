# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        
        temp_node = root.left
        root.left = root.right
        root.right = temp_node

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root
        
        




























