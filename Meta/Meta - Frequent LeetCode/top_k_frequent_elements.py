class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        topK = {}
        maximum = 0
        
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
                
            if counter[n] > maximum:
                maximum = counter[n]
                
            if counter[n]-1 in topK:
                topK[counter[n]-1].discard(n)
                
            if counter[n] in topK:
                topK[counter[n]].add(n)
            else:
                topK[counter[n]] = {n}
            
        returnList = []    
        for i in range(0,maximum+1):
            length = len(returnList)
            if maximum - i in topK:
                returnList.extend(list(topK[maximum - i])[:k-length])
                
            if length == k:
                return returnList