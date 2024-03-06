class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counter = 0
        curCounter = 0
        for i in range(len(nums)):
            curCounter = nums[i] % 2
            if k == 1 and curCounter == k:
                counter += 1

            for j in range(i + 1, len(nums)):
                curCounter += nums[j] % 2

                if curCounter == k:
                    counter += 1
        return counter
