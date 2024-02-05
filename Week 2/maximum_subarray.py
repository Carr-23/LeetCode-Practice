class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        sum = 0
        largestSum = nums[i]
        for j in range(len(nums)):
            sum += nums[j]

            if nums[j] > sum:
                i = j
                sum = nums[j]

            if sum > largestSum:
                largestSum = sum

            # if sum - nums[j] > largestSum:
            #     sum -= nums[i]
            #     i += 1
            #     largestSum = sum
            #     print('te')

        return largestSum
