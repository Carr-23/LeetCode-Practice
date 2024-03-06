class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arrList = arr[:]
        counter = 0
        for a in sorted(arr):
            if a == 0:
                if a in arrList:
                    arrList.remove(a)
                if a in arrList:
                    arrList.remove(a)
                    counter += 1
            if a in arrList and a * 2 in arrList:
                arrList.remove(a)
                arrList.remove(a * 2)
                counter += 1

        return counter * 2 == len(arr)
