# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sumVal = self.helper(root, str(root.val))

        return sumVal

    def helper(self, root: Optional[TreeNode], string: str) -> int:
        leftVal = 0
        rightVal = 0
        if root.left is not None:
            leftVal = self.helper(root.left, string + str(root.left.val))
        
        if root.right is not None:
            rightVal = self.helper(root.right, string + str(root.right.val))

        if not root.right and not root.left:
            return int(string)
        
        return leftVal + rightVal