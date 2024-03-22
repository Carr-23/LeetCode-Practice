import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)

        return heapq.nlargest(k,nums)[-1]
