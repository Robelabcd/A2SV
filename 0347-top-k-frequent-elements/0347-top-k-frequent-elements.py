from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in nums
        count = Counter(nums)
        
        # Use a heap to get the k elements with the highest frequencies
        return heapq.nlargest(k, count.keys(), key=count.get)
