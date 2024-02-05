# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        _, max = self.search(root, 0)
        return max

    def search(self, root: Optional[TreeNode], curMax: int) -> Tuple[int, int]:
        if root is None:
            return 0, 0

        lengthL, maxL = self.search(root.left, curMax)
        lengthR, maxR = self.search(root.right, curMax)

        maxValue = lengthL + lengthR
        longest = max(lengthR, lengthL) + 1
        curMax = max(curMax, maxL, maxR, maxValue)

        return longest, curMax
