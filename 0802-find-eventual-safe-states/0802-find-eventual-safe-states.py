class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        terminal: no outgoing edge
        safe nods: all their edges lead to a terminal node

        use BfS topsort to solve this
            - reverse the direction of the edges
            - store the indegree of the nodes
                - safe nodes only have an incoming edges from the terminal ones
                - terminal ones has no incoming edges since it's reveresed 
            - append all the terminal nodes to a queue
            - pop them while reducing the indegree of their neighbour
                - if indegree == 0, append to the result
                - now the node becomes the new terminal
                    - append it to the queue

        '''

        #step 1: count the indegree of the nodes in reversing order
        indegree = [0]*len(graph)
        reversed_graph = [[] for _ in range(len(graph))]
        for node in range(len(graph)):
            
            for neigh in graph[node]:

                indegree[node] += 1
                reversed_graph[neigh].append(node)


        #step 2: store the terminal nodes to the queue
        #terminal - no incoming edge (since it's reversed)
        queue = deque()
        for node in range(len(graph)):

            if indegree[node] == 0:
                queue.append(node)

        result = []
        #step 3: start the BFS implementation
        while queue:

            terminal = queue.popleft()
            #append the node along the way
            result.append(terminal)


            for neigh in reversed_graph[terminal]:

                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    queue.append(neigh)  #the new terminal

        return sorted(result)


        


















