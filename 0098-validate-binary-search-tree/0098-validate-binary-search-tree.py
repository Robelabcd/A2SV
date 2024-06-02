# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        -inf < 2 < inf

        left: -inf < 1 < 2
        
        right: 2 < 3 < inf

        --> no child means it's valid (return True)

        ---> if not left and right requirements = not valid (return False)
        
        '''
        
        def helper(node, left_boundary, right_boundary):

            if not node:
                return True  

            if not (node.val > left_boundary and node.val < right_boundary):
                return False


            left = helper(node.left, left_boundary, node.val)
            right = helper(node.right, node.val, right_boundary)

            return left and right


        return helper(root, -inf, inf) #initially: -inf < node.val < inf


        

#Time complexity : O(2n) = O(n)  same with space complexity
