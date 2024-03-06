class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dupe = []
        pal = []
        length = 0
        for w in words:
            if w in pal:
                length += 4
                pal.remove(w)
                if w in dupe:
                    dupe.remove(w)
            else:
                pal.append(w[::-1])
                if w[0] == w[1]:
                    dupe.append(w)

        if dupe:
            return length + 2
        else:
            return length
