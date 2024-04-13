class Solution:
    def backtrack(self, close_p, open_p, stack, result):
        if close_p == 0:
            result.append(''.join(stack))

        if open_p:
            stack.append('(')
            self.backtrack(close_p, open_p - 1, stack, result)
            stack.pop()

        if close_p > open_p:
            stack.append(')')
            self.backtrack(close_p - 1, open_p, stack, result)
            stack.pop()

    def generateParenthesis(self, n):
        stack, result = [], []
        self.backtrack(n, n, stack, result)
        return result