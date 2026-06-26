# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        
        if (p and q is None) or (q and p is None):
            return False
        
        if p.val != q.val:
            return False
        
        left_sides = self.isSameTree(p.left, q.left)
        right_sides = self.isSameTree(p.right, q.right)

        return left_sides and right_sides 
        
        

            
        

       































    """


    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    
    """