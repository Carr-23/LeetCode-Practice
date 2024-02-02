# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return False if self.search(root, 0) == -2 else True

    def search(self, root: Optional[TreeNode], max: int) -> int:
        max1 = max
        max2 = max

        if root.left is not None:
            max1 = self.search(root.left, max1 + 1)
        if root.right is not None:
            max2 = self.search(root.right, max2 + 1)

        if abs(max1 - max2) > 1:
            return -2
        else:
            return max1 if max2 < max1 else max2
