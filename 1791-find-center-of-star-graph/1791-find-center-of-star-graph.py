class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        #second approach
        n = len(edges) + 1
        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)

        for x in edges:
            indegree[x[1]] += 1
            indegree[x[0]] += 1
            outdegree[x[1]] += 1
            outdegree[x[0]] += 1


        for i in range(len(indegree)):

            if indegree[i] == len(edges) and outdegree[i] == len(edges):
                return i


    '''
    Time and space complexity = O(n)
    '''