class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        res = 0
        mod = 10 ** 9 + 7

        for i, val in enumerate(arr):

            while stack and val < stack[-1][1]:
                
                j, m = stack.pop()

                left = j - stack[-1][0] if stack else j + 1
                right = i - j

                res = (res + m * left * right) % mod

            stack.append([i, val])

        for i in range(len(stack)):

            j, m = stack[i]

            left = j - stack[i-1][0] if i > 0 else j + 1
            right = len(arr) - j

            res = (res + m * left * right) % mod


        return res


