class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        matrix = []
        cur = []

        length = len(mat) * len(mat[0])

        if r * c != length:
            return mat

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                cur.append(mat[i][j])
                if len(cur) >= length / r:
                    matrix.append(cur)
                    cur = []

        return matrix
