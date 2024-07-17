class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        maze = grid[i][j]

            containg '.' --> empty  and  '+' --> wall

        entrance = (i, j) ---> starting point        
        
        result = min(possible_exits_distance)


        Approach:
            - search for all possible_exits
            - DFS or BFS from the entrance to each possible_exits
            - choose the shortest one 
        
        '''
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def inbound(x, y):

            return 0 <= x < len(maze) and 0 <= y < len(maze[0])

        
        
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))


        while queue:

            i, j, distance = queue.popleft()


            if (i in {0, len(maze)-1} or j in {0, len(maze[0])-1}) and [i, j] != entrance:
                    return distance


            for x, y in direction:

                dx, dy = i+x, j+y

                if inbound(dx, dy) and (dx, dy) not in visited and maze[dx][dy] == '.':
                    queue.append((dx, dy, distance+1))
                    visited.add((dx, dy))

        return -1 

