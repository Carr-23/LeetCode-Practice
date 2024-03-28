class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        lowestSeen = [nums[-1],length - 1]
        current = -1
        
        for i in range(length-2,-1,-1):
            if nums[i] < lowestSeen[0]:
                temp = nums[i]
                nums[i] = nums[lowestSeen[1]]
                nums[lowestSeen[1]] = temp
                current = i
                break
            elif nums[i] < lowestSeen[0]:
                lowestSeen[0] = nums[i]
                lowestSeen[1] = i

        print(nums)
        if current != -1:
            print('here2')
            for i in range(current+1,length-1):
                print(nums)
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    return
            return
        
        return nums.reverse()
    
    def getNextBiggest(self, value: int, dictionary: dict) -> int:
        