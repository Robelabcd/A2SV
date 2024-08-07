class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:

        heappush(self.heap, val)

        while len(self.heap) > self.k:
            heappop(self.heap)
        a = self.heap[0] 
        return a
        



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)