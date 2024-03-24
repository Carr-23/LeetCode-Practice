# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        seeList = []
        maxDepth = -1
        currentDepth = 0
        
        maxDepth, seeList = self.helper(root, maxDepth, currentDepth, seeList)
        
        return seeList
        
    def helper(self, root: Optional[TreeNode], maxDepth: int, currentDepth: int, seeList:list) -> (int,list):
        if currentDepth > maxDepth:
            seeList.append(root.val)
            
        if root.right is not None:
            maxDepth, seeList = self.helper(root.right, maxDepth, currentDepth+1, seeList)
        
        if root.left is not None:
            maxDepth, seeList = self.helper(root.left, maxDepth, currentDepth+1,seeList)
        
        if currentDepth > maxDepth:
            maxDepth = currentDepth
            
        return maxDepth,seeList