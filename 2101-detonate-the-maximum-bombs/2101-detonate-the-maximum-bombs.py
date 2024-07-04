class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        '''
        [A = [2,1,3], B = [6,1,4]]
        
        distance(A&B) <= radius -> can detonate 
        distance **2 = (x1 - x2)**2 + (y1 - y2)**2  -->pythagoras theorem 

        B can detonate A but not vice versa -> so, directed graph
        
        '''
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                distance = (x1-x2)**2 + (y1-y2)**2

                if distance <= r1**2:
                    graph[i].append(j)

                if distance <= r2**2:
                    graph[j].append(i)

        def dfs(node):
            stack = [node]
            visited = [0]*n
            visited[node] = 1
            count = 1
            while stack:
                u = stack.pop()     
                for neigh in graph[u]:
                    if visited[neigh]==0:
                        stack.append(neigh)
                        visited[neigh] = 1
                        count += 1

            return count

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))

        return ans
                