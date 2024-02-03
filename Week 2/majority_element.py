class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numHM = {}
        if len(nums) < 3:
            return nums[0]

        for n in nums:
            if n in numHM:
                numHM[n] += 1
                if numHM[n] > len(nums) / 2:
                    return n
            else:
                numHM[n] = 1
