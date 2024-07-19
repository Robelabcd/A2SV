# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        possible = False
        def helper(node, summ):
            nonlocal possible

            if node:
                summ += node.val
                if not node.left and not node.right:
                    if summ == targetSum:
                        possible = True

                    else:
                        summ -= node.val
                    

                helper(node.left, summ)
                helper(node.right, summ)


        helper(root, 0)
        return possible
