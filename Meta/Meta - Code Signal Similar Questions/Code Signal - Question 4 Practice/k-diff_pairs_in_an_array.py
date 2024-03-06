class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numsCount = collections.Counter(nums)
        numSet = set(nums)
        counter = 0
        for n in numSet:
            if numsCount[n] > 0:
                if k + n in numSet:
                    if k == 0 and numsCount[n] > 1:
                        counter += 1
                    elif k != 0:
                        counter += 1
        return counter
