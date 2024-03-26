class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        fp = len(num1) - 1
        sp = len(num2) - 1
        remainder = 0
        
        returnStr = ""
        
        while fp >= 0 or sp >= 0:
            if fp >= 0:
                digit1 = ord(num1[fp]) - 48
            else:
                digit1 = 0

            if sp >= 0:
                digit2 = ord(num2[sp]) - 48
            else:
                digit2 = 0

            sp -= 1
            fp -= 1
            
            sumValue = digit1 + digit2 + remainder
            remainder = sumValue // 10
            sumValue -= remainder * 10
            
            returnStr = str(sumValue) + returnStr
        
        if remainder:
            returnStr = str(remainder) + returnStr
        return returnStr