class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        '''
        - build the union find
            - find and union if the vertices exist
                - if true: this is the edge
            - else continue building 
    
        '''

        root = [i for i in range(len(edges)+1)]
        size = [1]*(len(edges)+1)

        def find(node_):
            x = root[node_]
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
       
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return True
        
            if size[rootX] > size[rootY]:
                root[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                root[rootX] = rootY
                size[rootY] += size[rootX]

            return False

        
        for node1, node2 in edges:

            if union(node1, node2):
                break

        return [node1, node2]

        


        