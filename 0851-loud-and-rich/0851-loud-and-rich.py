class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        '''
        graph - indegree

        indegree - 0

        bfs
         - if quiet(current node) < quietnes(neigh)
           res[neigh] = current_node
           
        '''

        graph = [[] for _ in range(len(quiet))]

        indegree = [0]*len(quiet)

        for source, destination in richer:

            graph[source].append(destination)
            indegree[destination] += 1

        q = deque()

        for i in range(len(quiet)):
            if indegree[i] == 0:
                q.append(i)


        res = [ind for ind in range(len(quiet))]
        while q:

            cur = q.popleft()

            for neigh in graph[cur]:

                indegree[neigh] -= 1

                if quiet[res[cur]] < quiet[res[neigh]]:
                    res[neigh] = res[cur]

                if indegree[neigh] == 0:
                    q.append(neigh)


        return res
















        