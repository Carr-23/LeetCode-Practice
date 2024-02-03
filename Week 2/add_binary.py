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

            if total == 2:
                sum += "0"
                remainder = 1
            elif total == 3:
                sum += "1"
                remainder = 1
            elif total == 1:
                sum += "1"
                remainder = 0
            else:
                sum += "0"
                remainder = 0

        return sum[::-1]
