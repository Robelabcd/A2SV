# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
        
            if not node:
                return []
        
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        
        def inorder_bst(values):
            
            if not values:
                return None
            
            mid = len(values) // 2
            root = TreeNode(values[mid])
            
            root.left = inorder_bst(values[:mid])
            root.right = inorder_bst(values[mid + 1:])
            
            
            return root
        
        
        '''
            1st - inorder list
            2ns - from list -> bst balanced
        
        '''
        sorted_values = inorder(root)
        

        return inorder_bst(sorted_values)