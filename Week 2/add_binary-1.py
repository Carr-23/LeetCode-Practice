class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count1 = len(a) - 1
        count2 = len(b) - 1
        remainder = 0
        sum = ""
        while count1 > -1 or count2 > -1 or remainder > 0:
            a1 = 0
            b1 = 0
            if count1 > -1:
                a1 = int(a[count1])
                count1 -= 1

            if count2 > -1:
                b1 = int(b[count2])
                count2 -= 1

            total = a1 + b1 + remainder

            sum += str(total % 2)
            remainder = total // 2

        return sum[::-1]
