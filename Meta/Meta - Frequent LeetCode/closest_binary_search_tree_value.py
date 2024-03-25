# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:        
        value,diff = self.helper(root,target,[root.val,abs(target-root.val)])

        return value
        
        
    def helper(self, root: Optional[TreeNode], target: float, closestNumber: list[float]) -> list[float]:
        if root is None:
            return closestNumber
    
        currentValue = [root.val, abs(target - root.val)]
        
        if currentValue[1] < closestNumber[1]:
            closestNumber = currentValue
        elif currentValue[1] == closestNumber[1]:
            closestNumber = currentValue if currentValue[0] < closestNumber[0] else closestNumber
    
        closestNumber = self.helper(root.right, target, closestNumber)
        closestNumber = self.helper(root.left, target, closestNumber)
            
        return closestNumber
        