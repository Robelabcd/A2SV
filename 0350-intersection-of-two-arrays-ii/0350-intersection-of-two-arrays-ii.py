from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictt = defaultdict(int)
        
        for num in nums2:
            dictt[num] += 1

        result = []
        
        for num in nums1:
            if dictt[num] > 0:
                result.append(num)
                dictt[num] -= 1
        
        return result

                  

                

