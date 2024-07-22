class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        ''' 
        
        indegree: 0  1  2  0  1  1
        outdegree: 2  0 1  1  1  0
    
        '''

        indegree = [0]*n
        result = []

        for _, i in edges:
            indegree[i] += 1
            
        for i in range(n):
            if(indegree[i]==0):
                result.append(i)

        return result
    