# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        min_count = inf
        def helper(node, distance):

            nonlocal min_count

            if node:
                if not node.left and not node.right:
                    min_count = min(min_count, distance)


                helper(node.left, distance+1)
                helper(node.right, distance+1)


        helper(root, 1)

        return min_count if min_count != inf else 0



