# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        '''
        LCA - to be found given values : p and q ---> the two nodes

        1. searching for the nodes
        2. once reached to the nodes:

        -> check if they are less than the root node
        go to the left side
        -> check if they are more than the root node
        go ro the righ side

        otherwise, return root node
        
        '''

        if p.val > root.val and q.val > root.val:

            return self.lowestCommonAncestor(root.right, p, q)

        if p.val < root.val and q.val < root.val:

            return self.lowestCommonAncestor(root.left, p, q)

        else:

            return root










