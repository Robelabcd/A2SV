# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #iterative and recursive approach
        '''
        #recursive approach
        res = []
        def in_order(node):

            if not node:
                return

            
            #inorder :  left -> root -> right

            in_order(node.left)
            res.append(node.val)
            in_order(node.right)


        in_order(root)
        return res
        '''

        #iterative approach - using a stack

        stack = []
        res = []

        cur_ptr = root  
        #we need to go all the way left while storing the nodes we touch in the stack

        while stack or cur_ptr:

            while cur_ptr:

                stack.append(cur_ptr)
                cur_ptr = cur_ptr.left    #to the leftmost side of the tree

            #pop from the stack to get the leftmost node
            cur_ptr = stack.pop()

            #store the value of the node
            res.append(cur_ptr.val)

            #incase the current leftmost node has right connection
            cur_ptr = cur_ptr.right


        return res
            























