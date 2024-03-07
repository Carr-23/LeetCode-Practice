class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        order = []
        i = j = 0
        up = True
        for k in range(len(mat) * len(mat[0])):
            order.append(mat[i][j])

            if up:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1

            if i < 0 and j < len(mat[0]):
                i += 1
                up = False
            elif i >= len(mat):
                i -= 1
                j += 2
                up = True
            elif j < 0 and i < len(mat):
                j += 1
                up = True
            elif j >= len(mat[0]):
                i += 2
                j -= 1
                up = False

        return order
