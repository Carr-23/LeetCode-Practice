# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        distanceFromRootLeft = {}
        distanceFromRootRight = {0:[root.val]}

        distanceFromRootLeft = self.helper(root.left,1,distanceFromRootLeft)
        distanceFromRootRight = self.helper(root.right,1,distanceFromRootRight)
        
        cur = -1
        returnList = []
        for d,v in distanceFromRootLeft.items():
            if target.val in v:
                cur = d
                returnList += [x for x in v if x != target.val]
                left = True
                break

        if cur == -1:
            for d,v in distanceFromRootRight.items():
                if target.val in v:
                    cur = d
                    returnList += [x for x in v if x != target.val]
                    left = False
                    break

        print(distanceFromRootLeft)
        print(distanceFromRootRight)
        

        for d,v in distanceFromRootLeft.items():
            if left and abs(cur - d) == k:
                returnList.extend(v)
            elif not left and abs(cur + d) == k:
                returnList.extend(v)

        for d,v in distanceFromRootRight.items():
            if left and abs(cur + d) == k:
                returnList.extend(v)
            elif not left and abs(cur - d) == k:
                returnList.extend(v)
        
        return returnList


    def helper(self, root: TreeNode, dist: int, distanceFromRoot: dict) -> dict:
        if root == None:
            return distanceFromRoot
        
        if dist in distanceFromRoot:
            distanceFromRoot[dist].append(root.val)
        else:
            distanceFromRoot[dist] = [root.val]

        distanceFromRoot = self.helper(root.left, dist+1, distanceFromRoot)
        distanceFromRoot = self.helper(root.right, dist+1, distanceFromRoot)

        return distanceFromRoot