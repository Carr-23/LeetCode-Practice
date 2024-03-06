class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        modVals = {}
        counter = 0
        for t in time:
            calc = t % 60
            if 60 - calc in modVals:
                counter += modVals[60 - calc]

            calc = 60 if calc == 0 else calc
            if calc in modVals:
                modVals[calc] += 1
            else:
                modVals[calc] = 1

        return counter
