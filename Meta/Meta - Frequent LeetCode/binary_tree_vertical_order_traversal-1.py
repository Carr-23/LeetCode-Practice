# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Dict, Optional, List


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [[root, 0]]
        valDict = {}
        while queue:
            rootList = queue.pop(0)
            root, col = rootList
            if root is None:
                continue

            if col in valDict:
                valDict[col].append(root.val)
            else:
                valDict[col] = [root.val]

            queue.append([root.left, col - 1])
            queue.append([root.right, col + 1])

        return dict(sorted(valDict.items())).values()
