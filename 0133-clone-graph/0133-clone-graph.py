"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        '''
        step 1:  create a hashmap (old -> new) to check the visited node
        step 2:  append the neighbor
        '''
        
        #step 1: hashmap (old -> new)
        visited = {}

        def dfs(node):
            
            #step 3: node is already clone, so no need to clone again
            if node in visited:
                return visited[node]

            #step 2: create a clone not in visited
            cloned_node = Node(node.val)
            visited[node] = cloned_node     #old -> new


            #step 4: append the neighbors to the cloneed_node
            for neigh in node.neighbors:
                
                cloned_node.neighbors.append(dfs(neigh))
            
            #step 5
            return cloned_node 


        return dfs(node) if node else None




















