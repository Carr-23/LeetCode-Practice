class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        value = 1.0

        if n < 0:
            n = -n
            x = 1.0/x

        if n % 2 != 0:
            for i in range(int((n-1)/2)):
                value *= x

            value = value * value * x
        else:
            for i in range(int(n/2)):
                value *= x

            value = value * value

        return value