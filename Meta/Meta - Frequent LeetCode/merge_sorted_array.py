class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        fp = m-1
        sp = n-1
        listP = m+n-1
        
        while fp >= 0 and sp >= 0:
            if nums1[fp] >= nums2[sp]:
                nums1[listP] = nums1[fp]
                listP -= 1
                fp -= 1
            else:
                nums1[listP] = nums2[sp]
                listP -= 1
                sp -= 1

        while sp >= 0:
            nums1[listP] = nums2[sp]
            listP -= 1
            sp -= 1