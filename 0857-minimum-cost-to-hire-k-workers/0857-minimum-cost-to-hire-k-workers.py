class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ratios = [(wage[i] / quality[i], i) for i in range(n)]
        ratios.sort()
        
        total_quality = 0
        min_overall_cost = float('inf')
        max_heap = []
        
        for wage_proposition, idx in ratios:
            heapq.heappush(max_heap, -quality[idx])
            total_quality += quality[idx]
            
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            
            if len(max_heap) < k:
                continue
            
            current_overall_cost = total_quality * wage_proposition
            min_overall_cost = min(min_overall_cost, current_overall_cost)
                    
        return min_overall_cost