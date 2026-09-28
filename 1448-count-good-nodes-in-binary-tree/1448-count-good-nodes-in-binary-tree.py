# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        if not root:
            return 0

        
        self.good_node = 0
   
        def dfs(node, max_root_val):
            if node.val >= max_root_val:
                self.good_node += 1
            
            new_max = max(max_root_val, node.val)

            if node.left:
                dfs(node.left, new_max)
            
            if node.right:
                dfs(node.right, new_max)
            
        dfs(root, root.val)

        return self.good_node
            
        

            


        