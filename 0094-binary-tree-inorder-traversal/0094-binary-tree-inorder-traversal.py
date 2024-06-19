# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative approach

        res = []  #to store the final result

        stack = [] #to do the iterative process

        cur = root

        while cur or stack:

            #Go all the way to the left by pushing each node along the way
            while cur:
                
                stack.append(cur)
                cur = cur.left


            #now there is no left node - so pop and append to the result
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right      #check if there is right node 

        return res
        
                
        
        '''

        #recursive approach

        res = []

        def helper(root):

            if not root:
                return

            helper(root.left)
            res.append(root.val)
            helper(root.right)


        helper(root)

        return res

        '''