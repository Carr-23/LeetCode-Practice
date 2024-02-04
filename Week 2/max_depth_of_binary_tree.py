# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.search(root, 1, 1)

    def search(self, root: Optional[TreeNode], max: int, curMax: int) -> int:
        max1 = max
        max2 = max

        if root.left is not None:
            max1 = self.search(root.left, max1 + 1, curMax)
        if root.right is not None:
            max2 = self.search(root.right, max2 + 1, curMax)

        if max1 > curMax and max1 >= max2:
            return max1
        elif max2 > curMax:
            return max2
        else:
            return curMax
