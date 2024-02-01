class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHM = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in numsHM:
                return [numsHM[value], i]
            else:
                numsHM[num] = i
