class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        in_degree = [0]*n
        out_degree = [0]*n

        for node in trust:
            in_degree[node[1]-1] += 1
            out_degree[node[0]-1] += 1

        for i in range(len(in_degree)):

            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i + 1


        return -1



            