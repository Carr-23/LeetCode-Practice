class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        sums = {}
        for n1 in nums1:
            for n2 in nums2:
                sum = n1 + n2
                if sum not in sums:
                    sums[sum] = 1
                else:
                    sums[sum] += 1
        counter = 0
        for n3 in nums3:
            for n4 in nums4:
                sum = 0 - n3 - n4
                if sum in sums:
                    counter += sums[sum]
        return counter
