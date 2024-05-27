class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        summ = nums1 + nums2

        summ.sort()

        l = len(summ)

        if (l%2) == 0:
            median = l//2

            return (summ[median-1]+summ[median])/2

        else:
            median = l//2 
    
            return summ[median]