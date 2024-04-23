class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = [0]
        count = 0

        for element in s:

            if element == "(":
                stack.append(0)

            else:

                count = 2 * stack.pop()

                if count == 0:
                    count = 1

                stack[-1] = stack[-1] + count

        
        return stack[-1]

'''
worst case - O(n/2)
((((((((((   ))))))))))   -->appending first and popping later

best case - O(1)
()()()    ----> appending and popping each time

'''