class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # there is hidden edge case to return node 0 if no edge at all
        if not edges:
            return [0]
        # structure the undirected graph
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        # count the neighbors
        nei_map = {}
        leaves = deque()
        # each layer is marked with a level, and there is a max layer that contains center node
        layer_map = defaultdict(set)
        max_layer = 0
        for node in graph:
            num_neighbors = len(graph[node])
            if num_neighbors == 1:
                leaves.append((0,node))
                layer_map[0].add(node)
            nei_map[node] = num_neighbors

        # get rid of the leaves, gradually, until there is only 1 or 2 node
        while leaves:
            layer, node = leaves.popleft()
            max_layer = max(layer, max_layer)
            layer_map[layer].add(node)

            for nei in graph[node]:
                nei_map[nei] -= 1
                # we're get rid of the node, so that mean there is only n - 1 node left
                if nei_map[nei] == 1:
                    leaves.append((layer + 1,nei))
        return list(layer_map[max_layer])
            



            