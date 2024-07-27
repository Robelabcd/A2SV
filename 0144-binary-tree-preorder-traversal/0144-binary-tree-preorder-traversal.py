# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        preorder: root->left->right

        res = [] to store the result

        steps:
        append the root to "res" while going to the left

        append the right to "stack" along the way

        e.g
        root = [1, null, 2, 3]

        Append '1' to res and apend '2' to stack
        Go to left:
            if node exists:
                new_root = node
            else:
                new_root = stack.pop ---> go to right

        
        '''

        #using flag with each node

        stack = [(root, False)]  #initialize with root node and visited->as False

        res = []

        while stack:

            node, visited = stack.pop()

            if node:

                if visited:
                    #no need to go to its other connection since they're already in the stack
                    res.append(node.val)

                else:
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
                    

        return res



















