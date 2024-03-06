class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsList = {}
        maxVal = 0
        for n in nums:
            if n in numsList:
                continue

            if n - 1 in numsList and n + 1 in numsList:
                maxNum = numsList[n - 1] + numsList[n + 1] + 1
                numsList[n - 1] = maxNum
                numsList[n + 1] = maxNum
                numsList[n] = maxNum
                numsList = self.helper(numsList, maxNum, n - 1, False)
                numsList = self.helper(numsList, maxNum, n + 1, True)
            elif n - 1 in numsList:
                numsList[n - 1] += 1
                numsList[n] = numsList[n - 1]
                numsList = self.helper(numsList, numsList[n - 1], n - 1, False)
            elif n + 1 in numsList:
                numsList[n + 1] += 1
                numsList[n] = numsList[n + 1]
                numsList = self.helper(numsList, numsList[n + 1], n + 1, True)
            elif n not in numsList:
                numsList[n] = 1

            maxVal = max(maxVal, numsList[n])

        return maxVal

    def helper(self, numsList: dict, maxNum, n: int, direction: bool) -> dict:
        if not direction and n - 1 in numsList:
            numsList[n - 1] = maxNum
            numsList = self.helper(numsList, maxNum, n - 1, direction)

        if direction and n + 1 in numsList:
            numsList[n + 1] = maxNum
            numsList = self.helper(numsList, maxNum, n + 1, direction)

        return numsList
