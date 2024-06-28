class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #itertive approach

        
        visited = set() #to avoid cycle - contains visited nodes
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)  #graph = {node1: [node2], node2: []}
            graph[node2].append(node1)

        
        stack = [source]  #no recursive, we need our own stack

        while stack:

            node = stack.pop()

            if node == destination:
                return True

            for neigh in graph[node]:

                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)

        return False