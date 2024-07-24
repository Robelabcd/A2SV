# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        target --> Target node. 
            -->find nodes k away from the target node

        maximum edge to one node - 3
            ->left and right
            ->parent node

        How to access the parent node?
            -> create a hashmap = parent_dictt  
                parent_dictt[chile_node] = parent

        BFS:
            -> (target, 0) = (target_value, distance)
            -> Iterate through and collect the nodes k away from the target

        '''

        # from collections import defaultdict
        parent_dictt = defaultdict()

        def helper(node, parent):

            if not node:
                return 

            child_node = node
            parent_dictt[child_node] = parent

            new_parent = child_node
            helper(child_node.left, new_parent)
            helper(child_node.right, new_parent)

        helper(root, None)



        #BFS
        # from collections import deque
        queue = deque()
        visited = set()

        #append the the target to queue and start iterating until k away
        queue.append((target, 0))  #initial distance = 0
        visited.add(target)


        result = []
        while queue:

            node, distance = queue.popleft()

            if distance == k:
                result.append(node.val)

            if distance < k:

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append((node.left, distance+1))

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append((node.right, distance+1))

                if parent_dictt[node] and parent_dictt[node] not in visited:
                    visited.add(parent_dictt[node])
                    queue.append((parent_dictt[node], distance+1))

        return result











