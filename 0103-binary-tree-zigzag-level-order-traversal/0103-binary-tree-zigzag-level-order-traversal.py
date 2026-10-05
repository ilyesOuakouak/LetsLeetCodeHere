# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque([root])
        result = []
        level = 0

        while queue:
            size = len(queue)
            level += 1
            level_result = []
            
            

            for _ in range(size):
                current_node = queue.popleft()
                level_result.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)
                
            if level % 2 != 0:
                result.append(level_result)
            else:
                result.append(list(reversed(level_result)))
            
        return result
                

