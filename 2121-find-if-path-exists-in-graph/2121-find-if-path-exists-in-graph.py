class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        '''
        - a graph:
            --> bi-directional edges
            --> source and destination given
                - find if a path exist

        
        1. Using DFS - recusrion method
                     - iterative method
        2. Using BFS
                - deque (double ended queue) 
        
        '''
        # DFS - recursion method
        '''
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs_path(node):

            if node == destination:
                return True


            for neigh_node in graph[node]:
                if neigh_node not in visited:
                    visited.add(neigh_node)
                    if dfs_path(neigh_node):
                        return True

            return False


        return dfs_path(source)
        '''

        #DFS - iterative method

        '''
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        stack = [source]

        while stack:

            node = stack.pop()
            if node == destination:
                return True

            for neigh_node in graph[node]:
                if neigh_node not in visited:
                    visited.add(neigh_node)
                    stack.append(neigh_node)
        return False
        '''


        #BFS - deque
        from collections import deque

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        q = deque()
        q.append(source)

        while q:

            node = q.popleft()

            if node == destination:
                return True

            for neigh_node in graph[node]:
                if neigh_node not in visited:
                    visited.add(neigh_node)
                    q.append(neigh_node)


        return False




        #Time and Space for all: O(N+E)
            # N - number of nodes   E - number edges











                





















