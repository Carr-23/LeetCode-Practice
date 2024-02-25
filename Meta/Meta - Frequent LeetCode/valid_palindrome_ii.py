class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isPalin(s, True)

    def isPalin(self, s: str, delStat: bool) -> bool:
        if len(s) <= 1:
            return True
        j = len(s) - 1
        i = 0

        while i < j:
            if s[i] != s[j]:
                if delStat and self.isPalin(s[i + 1 : j + 1], False):
                    return True
                elif delStat and self.isPalin(s[i:j], False):
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True
