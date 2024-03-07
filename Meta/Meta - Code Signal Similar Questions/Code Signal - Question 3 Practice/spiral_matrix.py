class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrixVisited = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]

        order = []

        pi = pj = 0
        i = 0
        j = 0
        mj = 1
        mi = 0
        for k in range(len(matrix) * len(matrix[0])):
            order.append(matrix[i][j])
            matrixVisited[i][j] = True

            pi = i
            pj = j
            i += mi
            j += mj

            if (
                j >= len(matrix[0])
                or j < 0
                or i >= len(matrix)
                or i < 0
                or matrixVisited[i][j]
            ):
                i = pi
                j = pj
                mi, mj = mj, -mi
                pi = i
                pj = j
                i += mi
                j += mj
        return order
