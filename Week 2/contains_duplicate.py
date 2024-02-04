class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsHM = set()
        for n in nums:
            if n in numsHM:
                return True
            else:
                numsHM.add(n)
