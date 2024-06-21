class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        '''
        trust = [[1,3],[2,3]]

        1 ----> 3 <----- 2       #graph

                   1     2     3
        indegree:  0     0     2
        outdegree: 1     1     0
        
        3 trusts nobody == (outdegree[3]==0)

        everyone trusts 3 == (indegree[3] == len(graph)-1)

        so, 3 is the town judge


        '''

        if n == 1:
            return 1

        #initialize indegree and outdegree lists

        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for each in trust:
            trustor, trustee = each[0], each[1]

            outdegree[trustor] += 1
            indegree[trustee]  += 1


        for node, val in enumerate(indegree):

            if val == n - 1:

                if outdegree[node] == 0:

                    return node

        return -1


















