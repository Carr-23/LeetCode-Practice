"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        p1 = p
        q1 = q

        while p1 != q1:
            if q1 is None:
                q1 = p
            else:
                q1 = q1.parent

            if p1 is None:
                p1 = q
            else:
                p1 = p1.parent
        return p1
