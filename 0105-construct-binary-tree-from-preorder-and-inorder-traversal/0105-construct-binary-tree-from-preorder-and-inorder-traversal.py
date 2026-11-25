# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """ O(n) time """
        idx = {val: i for i, val in enumerate(inorder)}  
        pre = 0                                          

        def build(left, right):           
            nonlocal pre
            if left > right:               # empty range → no node
                return None

            root_val = preorder[pre]       # next root, in preorder order
            pre += 1
            root = TreeNode(root_val)

            mid = idx[root_val]            # O(1) instead of .index()
            root.left = build(left, mid - 1)    # everything left of mid in inorder
            root.right = build(mid + 1, right)  # everything right of mid
            return root

        return build(0, len(inorder) - 1)

        """ O(n2) time

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        i = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:1+i], inorder[:i])
        root.right = self.buildTree(preorder[1+i:], inorder[i+1:])

        return root

        """