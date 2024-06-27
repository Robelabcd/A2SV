# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #iterative approach

        res = [] 
        
        stack = []

        cur = root

        while cur or stack:

            if cur:
                #append the root and store the right nodes along the way
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left              #and go to the left node 
        
            else:

                cur = stack.pop()    #if cur is null, we need to pop back to previous nodes  


        return res
        
        
        '''
        recursive approach 

        res = []

        def helper(root):

            if not root:
                return

            res.append(root.val)

            helper(root.left)

            helper(root.right)


        helper(root)

        return res

        '''
        
    