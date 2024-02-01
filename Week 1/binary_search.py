class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maxNum = len(nums) - 1
        minNum = 0
        while minNum < maxNum:
            midpoint = int((maxNum + minNum) / 2)

            if nums[midpoint] == target:
                return midpoint

            if target < nums[midpoint]:
                maxNum = midpoint
            else:
                minNum = midpoint

        return False
