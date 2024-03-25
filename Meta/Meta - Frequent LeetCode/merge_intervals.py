class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        fp = 0
        sp = 1
        
        while fp < len(firstList) and sp < len(secondList):
            
            a0, a1 = intervals[fp]
            b0, b1 = intervals[sp]
            
            if a1 >= b0 or b1 >= a0:
                tempList = [min(b0,a0), max(b1,a1)]
                lowi = min(fp,sp)
                highi = max(fp,sp)
                
                intervals[lowi] = tempList
                del intervals[highi]
            else:
                fp += 1
                sp += 1
                
        return intervals
