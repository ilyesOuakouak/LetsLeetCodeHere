
class Solution(object):
    def kthSmallest(self, root, k):
        self.remained_k = k
        self.kth_node = 0

        def dfs(node):
            
            if node.left:
                dfs(node.left)

            self.remained_k -= 1

            if self.remained_k == 0:
                self.kth_node = node.val

            if node.right:
                dfs(node.right)

        dfs(root)

        return self.kth_node