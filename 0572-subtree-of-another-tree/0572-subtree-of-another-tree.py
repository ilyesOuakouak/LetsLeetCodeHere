# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def sameTree(a, b):
            if not a and not b:
                return True
            
            if a is None or b is None:
                return False
            
            if a.val != b.val:
                return False
           
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)
    
        # base case: what if root becomes None before finding a match?
        if not root:
            return False
        
        if sameTree(root, subRoot):
            return True
        
        # otherwise, keep searching — where else could subRoot be hiding?
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        