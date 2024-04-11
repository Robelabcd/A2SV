class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #let's use the stack operation to solve
        #whenever we encounter an operation we pop elements and do the calculation


        stack = []
        result = 0

        for i in range(len(tokens)):

            if tokens[i] == '+':
                x = stack.pop()
                y = stack.pop()
                result = (y+x)
                stack.append(result)

            elif tokens[i] == '-':
                x = stack.pop()
                y = stack.pop()
                result = (y - x)
                stack.append(result)

            elif tokens[i] == '*':
                x = stack.pop()
                y = stack.pop()
                result = (y * x)
                stack.append(result)

            elif tokens[i] == '/':
                x = stack.pop()
                y = stack.pop()
                result = int(y / x)
                stack.append(result)

            else:

                number = int(tokens[i])
                stack.append(number)


        return stack[-1]
