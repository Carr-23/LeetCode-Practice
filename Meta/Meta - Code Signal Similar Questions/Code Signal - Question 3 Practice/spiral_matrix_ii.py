class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrixVisited = [[0 for x in range(n)] for y in range(n)]

        pi = pj = 0
        i = 0
        j = 0
        mj = 1
        mi = 0
        for k in range(1, n**2 + 1):
            matrixVisited[i][j] = k

            pi = i
            pj = j
            i += mi
            j += mj

            if (
                j >= len(matrixVisited[0])
                or j < 0
                or i >= len(matrixVisited)
                or i < 0
                or matrixVisited[i][j] != 0
            ):
                i = pi
                j = pj
                mi, mj = mj, -mi
                pi = i
                pj = j
                i += mi
                j += mj

        return matrixVisited
