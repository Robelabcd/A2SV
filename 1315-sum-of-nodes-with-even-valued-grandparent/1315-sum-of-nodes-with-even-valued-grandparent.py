# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def helper(node):
            if not node:
                return 0

            ans = 0
            if (node.val%2==0) and node.left:
                if node.left.left:
                    ans += node.left.left.val
                
                if node.left.right:
                    ans += node.left.right.val

            if (node.val%2==0) and node.right:
                if node.right.left:
                    ans += node.right.left.val
                
                if node.right.right:
                    ans += node.right.right.val

            ans += helper(node.left)
            ans += helper(node.right)

            return ans


        return helper(root) 