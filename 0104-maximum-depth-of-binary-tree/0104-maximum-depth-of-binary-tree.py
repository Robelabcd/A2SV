# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         if root is None:

#             return 0
        
#         def left(node):

#             if node is None:
#                 return 0
            
#             return 1 + left(node.left)

#         def right(node):

#             if node is None:
#                 return 0

#             return 1 + right(node.right)

        
#         l = left(root)
#         r = right(root)

#         return max(l, r) + 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def depth(node):
            if node is None:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            return max(l, r) + 1

        return depth(root)
