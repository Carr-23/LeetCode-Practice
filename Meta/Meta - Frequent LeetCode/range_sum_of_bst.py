# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.sumHelper(root, low, high, 0)

    def sumHelper(
        self, root: Optional[TreeNode], low: int, high: int, sumT: int
    ) -> int:
        if root is not None:
            sumT = self.sumHelper(root.left, low, high, sumT)
            sumT = self.sumHelper(root.right, low, high, sumT)

            if root.val >= low and root.val <= high:
                return sumT + root.val

        return sumT
