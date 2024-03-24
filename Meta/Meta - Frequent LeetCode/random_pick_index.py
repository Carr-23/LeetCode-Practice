import random
class Solution:

    def __init__(self, nums: List[int]):
        self.numsIndex = {}

        for i,n in enumerate(nums):
            if n in self.numsIndex:
                self.numsIndex[n].append(i)
            else:
                self.numsIndex[n] = [i]
                
    def pick(self, target: int) -> int:
        if target in self.numsIndex:
            targetList = self.numsIndex[target]
            rng = random.randint(0, len(targetList)-1)
            return targetList[rng]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)