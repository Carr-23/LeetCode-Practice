class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        arrDict = collections.Counter(arr)
        counter = 0
        for i in arrDict:
            for j in arrDict:
                k = target - i - j
                if i <= j <= k and k in arrDict:
                    count = 0
                    if i == j == k:
                        count = (arrDict[i] * (arrDict[i] - 1) * (arrDict[i] - 2)) // 6
                    elif i == j != k:
                        count = (arrDict[i] * (arrDict[i] - 1) * arrDict[k]) // 2
                    elif i < j == k:
                        count = (arrDict[i] * arrDict[j] * (arrDict[j] - 1)) // 2
                    elif i < j < k:
                        count = arrDict[i] * arrDict[j] * arrDict[k]
                    counter += count

        return counter % 1_000_000_007
