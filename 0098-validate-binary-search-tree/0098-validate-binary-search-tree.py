# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        self.upper = float('inf')
        self.lower = float('-inf')

        def dfs(node, bottom, top):
            if node.val >= top or node.val <= bottom:
                return False
            
            left = dfs(node.left, bottom, node.val) if node.left else True
            right = dfs(node.right, node.val, top) if node.right  else True

            return left and right
        
        return dfs(root, self.lower, self.upper)

            
        
        
        

        


         

    

            

  
        