class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        visited = [-1] * n

        def helper(node, assign):
            visited[node] = assign

            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    if not helper(neighbor, 1-assign):
                        return False

                elif visited[neighbor] == visited[node]:
                    return False

            return True

        for node in range(n):

            if visited[node] == -1:

                if not helper(node, 0):
                    return False

        return True