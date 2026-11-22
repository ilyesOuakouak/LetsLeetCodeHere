# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root                      

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:             
            return root     
                             
        return left or right                  
        """
        def path_to(root: TreeNode, target: int, path: list[TreeNode])-> bool:
            if root is None:
                return False

            path.append(root)

            if root.val == target:
                return True
            
            if path_to(root.left, target, path) or path_to(root.right, target, path):
                return True
            
            path.pop()

            return False 

        path_p, path_q = [], []
        path_to(root, p.val, path_p)
        path_to(root, q.val, path_q)

        
        lca = None
        for a, b in zip(path_p, path_q):
            if a is not b:
                break
            lca = a
        return lca
        """
        


        