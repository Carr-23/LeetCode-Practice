# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Dict, Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictVal = self.verticalHelper(root, 0, {})
        dictVal = dict(sorted(dictVal.items()))

        return dictVal.values()

    def verticalHelper(self, root: Optional[TreeNode], col: int, valDict: Dict) -> Dict:
        if root is None:
            return valDict

        if col in valDict:
            valDict[col].append(root.val)
        else:
            valDict[col] = [root.val]

        valDict = self.verticalHelper(root.left, col - 1, valDict)
        valDict = self.verticalHelper(root.right, col + 1, valDict)

        return valDict
