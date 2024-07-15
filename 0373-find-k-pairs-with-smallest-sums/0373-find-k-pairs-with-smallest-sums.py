import heapq
from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if not nums1 or not nums2 or k <= 0:
            return []

        # Min-heap to keep track of the pairs with the smallest sums
        min_heap = []
        for i in range(min(len(nums1), k)):
            # Push the initial pairs (nums1[i], nums2[0]) into the heap
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        res = []
        while k > 0 and min_heap:
            # pop the smallest pair from the heap
            _, i, j = heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            k -= 1

            # If there is a next element in nums2, push the new pair (nums1[i], nums2[j+1]) into the heap
            if j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res