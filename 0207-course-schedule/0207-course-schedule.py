class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        visited = ['W'] * numCourses

        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)

        
        def dfs(node):
            
            if visited[node] == 'G':
                return False

            visited[node] = 'G' 

            for neigh in graph[node]:

                if visited[neigh] == 'W':

                    dfs(neigh)

                elif visited[neigh] == 'G':
                    return False
            
            visited[node] = 'B'
            return True


        for i in range(numCourses):

            if not dfs(i):
                return False

        return True
        