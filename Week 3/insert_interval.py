import math


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        minV = newInterval[0]
        maxV = newInterval[1]

        i = -1
        j = len(intervals)
        iFound = False
        jFound = False

        for x in range(math.ceil(len(intervals) / 2)):
            if minV <= intervals[x][1] and minV >= intervals[x][0]:
                i += 1
                iFound = True

            if minV <= intervals[x][0]:
                i += 0.5
                iFound = True

            if maxV <= intervals[j - 1 - x][1] and maxV >= intervals[j - 1 - x][0]:
                j -= 1
                jFound = True

            if maxV >= intervals[j - 1 - x][1]:
                j -= 0.5
                jFound = True

            i += 1
            j -= 1

            if iFound and jFound:
                minV = newInterval[0]
                maxV = newInterval[1]
                if (int)(i * 10) % 10 == 0:
                    minV = intervals[i][0]

                if (int)(j * 10) % 10 == 0:
                    minV = intervals[j][0]

                print(minV)
                print(maxV)

                return intervals.insert(math.ceil(i), [minV, maxV])
