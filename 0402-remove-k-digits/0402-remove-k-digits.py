class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Remove digits from the stack if they make the current number smaller
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining digits from the stack if k > 0
        while k > 0:
            stack.pop()
            k -= 1
        
        # Join the digits in the stack to form the smallest number
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'


            
        return '0' if result == inf else str(result)

            

