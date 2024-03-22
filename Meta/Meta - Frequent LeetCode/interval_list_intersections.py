class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        fp = 0
        sp = 0
        returnList = []
        while fp < len(firstList) and sp < len(secondList):
            a0, a1 = firstList[fp]
            b0, b1 = secondList[sp]

            if a0 <= b1 and b0 <= a1:
                returnList.append([max(a0,b0), min(a1,b1)])

            if a1 <= b1:
                fp += 1
            else:
                sp += 1

        return returnList
