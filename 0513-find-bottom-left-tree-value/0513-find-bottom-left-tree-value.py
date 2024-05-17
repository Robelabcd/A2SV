# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''

        [root]---> array

        [root.left, root.right]---> append this after popping the root

        simply, arr[0] will be the leftmost
        
        '''
        
        if not root:
            return None

        arr = [root]
        most_left = None

        while arr:

            lenn = len(arr)

            for i in range(lenn):

                node = arr.pop(0)   #the front one == left most

                if i == 0:
                    most_left = node.val

                if node.left:
                    arr.append(node.left)

                if node.right:
                    arr.append(node.right)


        return most_left