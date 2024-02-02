# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        maxNum = n
        minNum = 1
        while minNum <= maxNum:
            midpoint = int((maxNum + minNum) / 2)
            if isBadVersion(midpoint) and not isBadVersion(midpoint - 1):
                return midpoint

            if isBadVersion(midpoint):
                maxNum = midpoint - 1
            else:
                minNum = midpoint + 1
