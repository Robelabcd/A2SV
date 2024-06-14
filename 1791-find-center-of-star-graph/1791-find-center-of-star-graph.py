class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        '''
        indegree and outdegree of each
        [1:1, 2:3, 3:1, 4:1]

        2 - has n-1 edges 
        
        '''

        count_degree = defaultdict(int)

        for edge in edges:

            count_degree[edge[0]] += 1
            count_degree[edge[1]] += 1

        req = len(edges)

        for x, y in count_degree.items():
            if y == req:
                return x

            
            