class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        edge = defaultdict(int)
        
        for u, v in roads:
            edge[u] += 1
            edge[v] += 1
        
        maxx = 0
        
        for u in range(n):
            for v in range(u + 1, n):
                
                r = edge[u] + edge[v]
                
                if ([u, v]) in roads or ([v, u]) in roads:
                    r -= 1
                
                maxx = max(maxx, r)
        
        return maxx  