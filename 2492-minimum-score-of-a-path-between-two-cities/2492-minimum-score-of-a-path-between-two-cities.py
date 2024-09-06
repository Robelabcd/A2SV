class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = [i for i in range(size)]
                self.rank = [1] * size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  #
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.parent[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1
        
        uf = UnionFind(n + 1)
        
        for a, b, dist in roads:
            uf.union(a, b)
        
        result = float('inf')
        
        for a, b, dist in roads:
            if uf.find(1) == uf.find(a):  # Both cities should be in the same component as city 1
                result = min(result, dist)
        
        return result
