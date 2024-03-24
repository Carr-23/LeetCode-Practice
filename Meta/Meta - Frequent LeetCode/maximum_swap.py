import math
class Solution:
    def maximumSwap(self, num: int) -> int:

        if num <= 11:
            return num
            
        nums = list(str(num))
        numsDict = {}
        
        for i,n in enumerate(nums):
            if n in numsDict:
                numsDict[n].append(i)
            else:
                numsDict[n] = [i]

        for i,n in enumerate(nums):

            if n in numsDict:
                if len(numsDict[n]) > 1:
                    numsDict[n].remove(i)
                else:
                    del numsDict[n]
            
            if numsDict:
                maxValue = max(list(numsDict.keys()))
                
                if maxValue > n:
                    nums[i] = maxValue
                    nums[numsDict[maxValue][-1]] = n
                    break
            
        return int("".join(nums))
        