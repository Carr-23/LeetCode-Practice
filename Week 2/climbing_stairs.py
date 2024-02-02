class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        n1 = 1
        n2 = 2

        for i in range(2, n):
            temp = n1
            n1 = n2
            n2 = temp + n2

        return n2
