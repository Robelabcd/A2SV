class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []

        for i in range(len(ops)):

            if ops[i] == '+':
                ans = stack[-1] + stack[-2]
                stack.append(ans)

            elif ops[i] == 'D':
                ans = stack[-1] + stack[-1]
                stack.append(ans)
            
            elif ops[i] == 'C':
                stack.pop()

            else:
                stack.append(int(ops[i]))

        res = 0
        for i in range(len(stack)):
            res += stack[i]

        return res

