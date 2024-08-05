from typing import List
import collections

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        '''
        - Compute the incoming degree for each node
        - Initialize a queue with nodes that have no incoming edges
        - Perform BFS to mark nodes reachable from nodes with no incoming edges
        - Find the longest cycle in the remaining unvisited nodes
        
        '''
        num_nodes = len(edges)
        is_visited = [False] * num_nodes
        incoming_degree = [0] * num_nodes

        #step 1
        for target in edges:
            if target != -1:
                incoming_degree[target] += 1
        
        #step 2
        zero_incoming_degree_queue = collections.deque()
        for node in range(num_nodes):
            if incoming_degree[node] == 0:
                zero_incoming_degree_queue.append(node)

        #step 3
        while zero_incoming_degree_queue:
            current_node = zero_incoming_degree_queue.popleft()
            is_visited[current_node] = True
            neighbor = edges[current_node]
            if neighbor != -1:
                incoming_degree[neighbor] -= 1
                if incoming_degree[neighbor] == 0:
                    zero_incoming_degree_queue.append(neighbor)

        
        longest_cycle_length = -1
        for node in range(num_nodes):
            if not is_visited[node]:
                cycle_length = 1
                is_visited[node] = True
                next_node = edges[node]

                # Traverse the cycle starting from the current node
                while next_node != node:
                    is_visited[next_node] = True
                    cycle_length += 1
                    next_node = edges[next_node]

                longest_cycle_length = max(longest_cycle_length, cycle_length)
        
        return longest_cycle_length
