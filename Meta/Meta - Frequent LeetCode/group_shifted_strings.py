class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        letterDistance = {}

        for s in strings:
            dist = []
            cur = ord(s[0])
            for i in range(1,len(s)):
                dist.append((cur-ord(s[i]))%26)
                cur = ord(s[i])

            dist = tuple(dist)

            if dist in letterDistance:
                letterDistance[dist].append(s)
            else:
                letterDistance[dist] = [s]
                
        returnList = []
        for l in letterDistance.values():
            returnList.append(l)

        return returnList