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
        '''
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
        '''
        
        #iterative - method 2
        
        '''
        using two stacks:
        - one to store the value
        - the other to traverse
        '''

        stack1 = [root]  #to traverse
        stack2 = []      #to store value along the way
        res = []

        while stack1:

            cur = stack1.pop()
            if cur:
                stack2.append(cur.val)  #NB: we're storing in the reverse order 
                                            #since root is the last element in postorder
            
            if cur and cur.right:
                stack1.append(cur.right)

            if cur and cur.left:
                stack1.append(cur.left)


        #we stored the values from back to front(root -> leftmost) - reversePostorder

        while stack2:
            node_val = stack2.pop()
            res.append(node_val)


        return res















































