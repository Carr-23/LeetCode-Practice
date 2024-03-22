import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        pointsList = {}

        for p in points:
            p0,p1 = p

            distance = sqrt((p0)**2 + (p1)**2)
            
            if distance in pointsList:
                pointsList[distance].append(p)
            else:
                pointsList[distance] = [p]

            heapq.heappush(heap, distance)

        returnList = []

        while len(returnList) < k:
            returnList += pointsList[heapq.heappop(heap)]

        return returnList