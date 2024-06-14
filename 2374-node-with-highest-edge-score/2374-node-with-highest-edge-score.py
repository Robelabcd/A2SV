class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        count_edge = defaultdict(int)

        for i in range(len(edges)):

            count_edge[edges[i]] += i


        maxx_val = -1
        minn_node = -1
        for node in count_edge:

            if count_edge[node] > maxx_val or (count_edge[node]==maxx_val and node < minn_node):
                maxx_val = count_edge[node]
                minn_node = node

        return minn_node


