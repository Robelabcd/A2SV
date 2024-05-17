# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        '''
        Required : maximum difference(MD)

        MD = | least minimum - highest maximum |

        Approach:

        searching the minimum and max value while traversing

        finally return |min - max|

        left side:
        min = max = 8

        min = 3 max = 8

        min = 1  max = 8

        min = 1 max = 8


        right side:

        min = max = 8

        min = 8 max = 10 

        min = 8 max = 14
        
        '''

        def helper(new_root, maximum, minimum):

            if new_root is None:
                return maximum - minimum   #base case


            else:

                maximum = max(maximum, new_root.val)
                minimum = min(minimum, new_root.val)

                x = helper(new_root.left, maximum, minimum)
                y = helper(new_root.right, maximum, minimum)

                ans = max(x, y)

                return ans

            

        if root is None:

            return 0

        else:

            return helper(root, root.val, root.val) #both max and min is the root











