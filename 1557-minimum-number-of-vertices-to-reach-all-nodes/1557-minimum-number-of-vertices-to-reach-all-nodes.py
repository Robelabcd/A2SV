class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        '''
        indegree: 0  1  2  0  1  1
        outdegree: 2  0 1  1  1  0
    
        '''

        indegree = [0]*n
        result = []

        for i in range(len(edges)):
            indegree[edges[i][1]] += 1

        for i in range(n):
            if(indegree[i]==0):
                result.append(i)

        return result
    