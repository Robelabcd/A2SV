# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #Recursive approach
        '''
        res = []

        def helper(root):

            if not root:
                return

            helper(root.left)
            
            helper(root.right)

            res.append(root.val)


        helper(root)

        return res
        '''
        # Iterative approach - using flag
        # Post order ---> left -> right -> root

        stack = [(root, False)]
        res = []

        while stack:
            node, visited = stack.pop()

            if node:
                if visited:
                    res.append(node.val)

                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return res



















