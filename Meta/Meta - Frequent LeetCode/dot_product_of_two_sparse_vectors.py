class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        dp = 0
        for i in range(len(vec.nums)):
            dp += vec.nums[i] * self.nums[i]
        return dp


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
