class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        maxVal = 0

        for n in nums:
            if n - 1 in nums:
                continue

            curVal = 1
            cur = n
            while cur + 1 in nums:
                curVal += 1
                cur += 1

            maxVal = max(curVal, maxVal)

        return maxVal
