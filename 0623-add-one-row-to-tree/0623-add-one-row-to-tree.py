# come back again and do it----you didn't do it properly


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: TreeNode, val: int, depth: int, currdepth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        if not root:
            return root

        if currdepth == depth - 1:
            leftman = root.left
            rightman = root.right

            root.left = TreeNode(val)
            root.right = TreeNode(val)

            root.left.left = leftman
            root.right.right = rightman
            return root

        root.left = self.helper(root.left, val, depth, currdepth + 1)
        root.right = self.helper(root.right, val, depth, currdepth + 1)

        return root

    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        return self.helper(root, val, depth, 1)