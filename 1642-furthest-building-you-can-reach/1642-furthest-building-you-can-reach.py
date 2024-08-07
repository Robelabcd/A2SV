from heapq import heappush, heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []

        for i in range(n-1):
            
            difference = heights[i+1] - heights[i]
            
            if difference > 0:

                heappush(heap, difference)

                size_heap = len(heap)
                if size_heap > ladders:
                    bricks -= heappop(heap)

                    if bricks < 0:
                        return i
        
        return n - 1
