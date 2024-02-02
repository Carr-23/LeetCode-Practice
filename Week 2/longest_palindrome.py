class Solution:
    def longestPalindrome(self, s: str) -> int:
        letHM = {}

        for s1 in s:
            if s1 in letHM:
                letHM[s1] += 1
            else:
                letHM[s1] = 1

        counter = 0
        odd = False
        for letter, count in letHM.items():
            if not odd and count % 2 != 0:
                counter += 1
                odd = True
            counter += int(count / 2) * 2

        return counter
