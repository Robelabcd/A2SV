# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #What if there is no tree
        if not root1 and not root2:
            return None

        #only tree 2
        elif not root1:
            return root2

        #only tree 1
        elif not root2:
            return root1

        combined = TreeNode(root1.val + root2.val)

        combined.left = self.mergeTrees(root1.left, root2.left)

        combined.right = self.mergeTrees(root1.right, root2.right)


        return combined












        