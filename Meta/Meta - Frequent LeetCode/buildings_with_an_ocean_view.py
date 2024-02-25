class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        idxList = []
        max = -1
        for i in range(n):
            if heights[n - i - 1] > max:
                max = heights[n - 1 - i]
                idxList.append(n - 1 - i)

        return idxList[::-1]
