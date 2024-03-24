class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        value = 1.0

        for i in range(abs(n)):
            value *= x

        if n < 0:
            value = 1.0/value
            
        return value