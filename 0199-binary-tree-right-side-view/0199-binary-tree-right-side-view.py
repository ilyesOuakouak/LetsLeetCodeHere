# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        
        result = []
        queue = deque([root])

        if not root:
            return []
        
        while queue:
            size = len(queue)
            

            for i in range(size):
                current_node = queue.popleft()

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                
                if i == size - 1:
                    result.append(current_node.val)
                
        return result



        