#learnt it from somewhere, come back and do it again after taking the lesson-----reminder





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.totalSum = 0 # Variable to store the total sum
    
    # Recursive function to calculate the sum of numbers formed by root to leaf paths
    def sumNumbersHelper(self, root: TreeNode, currentSum: int):
        # Base case: if the node is a leaf node
        if not root.left and not root.right:
            # Add the sum formed by the path from root to leaf to the total sum
            self.totalSum += currentSum * 10 + root.val
            return
        # Update the current sum by appending the current node's value
        currentSum *= 10
        currentSum += root.val
        # Recursively traverse the left and right subtrees if they are available
        if root.left:
            self.sumNumbersHelper(root.left, currentSum)
        if root.right:
            self.sumNumbersHelper(root.right, currentSum)

    # Function to calculate the sum of numbers formed by root to leaf paths
    def sumNumbers(self, root: TreeNode) -> int:
        # Start the recursive function with initial sum 0
        self.sumNumbersHelper(root, 0)
        # Return the total sum
        return self.totalSum  