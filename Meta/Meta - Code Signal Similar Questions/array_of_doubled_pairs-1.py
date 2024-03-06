class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        countMap = collections.Counter(arr)
        counter = 0
        for a in sorted(arr):
            if a == 0:
                if countMap[a] > 1:
                    countMap[a] -= 2
                    counter += 1
            elif countMap[a] > 0 and countMap[a * 2] > 0:
                countMap[a] -= 1
                countMap[a * 2] -= 1
                counter += 1

        return counter * 2 == len(arr)
