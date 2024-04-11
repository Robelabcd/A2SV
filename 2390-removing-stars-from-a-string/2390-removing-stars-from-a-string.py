class Solution:
    def removeStars(self, s: str) -> str:
        '''
Input: s = "leet**cod*e"
Output: "lecoe"

Goal: to remove the left element whenever we encounter '*'

Approach:

use a stack and pop the last element whenever we encounter

and convert the array back to string

        '''        


        stack = []
        for char in s:

            if char == '*':
                stack.pop()

            else:

                stack.append(char)

        return ''.join(stack)