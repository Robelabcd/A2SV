class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict()

        for index, relation in enumerate(equations):

            src, dest = relation[0], relation[1]

            weight = values[index]

            if src not in graph:
                graph[src] = {}    
            if dest not in graph:
                graph[dest] = {}

            graph[src][dest] = weight
            graph[dest][src] = 1 / weight

    
        result = [-1]*len(queries)

        def dfs(src, dest, visited):

            if src == dest:
                return 1

            visited.add(src)

            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    result = dfs(neighbor, dest, visited)
                    if result != -1:
                        return result * weight
            return -1

        
        for index, relation in enumerate(queries):
            src, dest = relation[0], relation[1]

            if src not in graph or dest not in graph:
                continue

            result[index] = dfs(src, dest, set())


        return result






