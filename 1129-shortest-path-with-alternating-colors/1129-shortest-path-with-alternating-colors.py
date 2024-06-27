class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        '''
        alternating color:
        A --- B --- C
         \
          \
           D --- E
        
        while traversing, the color of the edges should be alternating, otherwise distance = -1 

        so, distance from A = [0, 1, -1, 1, 2]

        1. two dictionaries for blue and red connections 

        2. to avoid cycle and check the alternating color ---> visited = ((node, color))

        3. BFS - deque() is required
         
        '''


        #build the connection
        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dest in redEdges:
            red[src].append(dest)

        for src, dest in blueEdges:
            blue[src].append(dest)

        
        #a set - to check whether it's visited
        visited= set()  #node and color
        visited.add((0, None))
        #queue to BFS
        q = deque()
        q.append([0, 0, None])

        #distance from the src - initially
        answer = [-1]*n


        while q:

            node, distance, color = q.popleft()
            
            if answer[node] == -1:
                answer[node] = distance

            
            if color != "RED":
                
                for neigh in red[node]:

                    if (neigh, "RED") not in visited:

                        visited.add((neigh, "RED"))

                        q.append([neigh, distance+1, "RED"])


            if color != "BLUE":

                for neigh in blue[node]:

                    if (neigh, "BLUE") not in visited:

                        visited.add((neigh, "BLUE"))

                        q.append([neigh, distance+1, "BLUE"])


        return answer


                    

            











