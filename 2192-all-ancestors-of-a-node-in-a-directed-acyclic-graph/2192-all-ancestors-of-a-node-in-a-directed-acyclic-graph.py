class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        #go to the node with zero outdegree and backtrack
        #while backtracking:
            # append the ancestor node


        graph = [[] for _ in range(n)]
        # indegree = [0] * n

        for destination, source in edges:  

            graph[source].append(destination)
            # indegree[destination] += 1

        
        result = []
        for node in range(len(graph)):

            visited = [0]*n
            
            queue = deque()
            
            queue.append(node)
            visited[node] = 1
        
            child_path = []
            while queue:

                node = queue.popleft()

                for neigh in graph[node]:
                    
                    if not visited[neigh]:
                        child_path.append(neigh)
                        queue.append(neigh)
                        visited[neigh] = 1

            result.append(sorted(child_path))


        return result

            