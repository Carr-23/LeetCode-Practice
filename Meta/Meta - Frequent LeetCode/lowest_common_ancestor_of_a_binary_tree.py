# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        return self.lcaHelper(root, p, q)

    def lcaHelper(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if root is None:
            return

        left = self.lcaHelper(root.left, p, q)
        right = self.lcaHelper(root.right, p, q)

        if root is p:
            return p
        elif root is q:
            return q

        if left and right:
            return root

        return right if left is None else left
