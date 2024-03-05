class Solution:
    def customSortString(self, order: str, s: str) -> str:
        newS = ""
        for o in order:
            while o in s:
                newS += o
                s = s.replace(o, "", 1)
        return newS + s
