# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        #using iterative approach

        current = root 

        while not(current is None):

            if current.val == val:
                return current 

            elif val < current.val:
                current = current.left

            elif val > current.val:
                current = current.right

        return None

        