class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower,upper]]

        numsSet = set(nums)
        ranges = []
        if nums[0] > lower:
            ranges.append([lower,nums[0]-1])
            
        for i in range(len(nums)-1):
            n = nums[i]
            if n+1 not in numsSet:
                ranges.append([n+1,nums[i+1]-1])
            
        if nums[-1] < upper:
            ranges.append([nums[-1]+1,upper])
            
        return ranges