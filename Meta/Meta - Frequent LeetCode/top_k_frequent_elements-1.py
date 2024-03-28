from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedNums = Counter(nums)
        values = list(countedNums.values())
        topK = set()
        
        heapq._heapify_max(values) 
        
        for i in range(k):
            topK.add(heapq._heappop_max(values))
            
        returnList = []
        for k,v in countedNums.items():
            if v in topK:
                returnList.append(k)
                
        return returnList