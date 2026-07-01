# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):

        if not root:
            return []
        
        result = []

        queue = deque([root])

        while queue:
            size_queue = len(queue)
            current_level = []
            for _ in range(size_queue):
                current_element = queue.popleft()

                if current_element:
                    current_level.append(current_element.val)

                    if current_element.left:
                        queue.append(current_element.left)
                    if current_element.right:
                        queue.append(current_element.right)
                
            result.append(current_level)

        return result






































