class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if i - 1 < 0:
                a = nums[i] - 1
            else:
                a = nums[i-1]
                
            b = nums[i]
            
            if i + 1 == len(nums):
                c = nums[i] - 1
            else:
                c = nums[i+1]
                
            if b > c and b > a:
                return i
        