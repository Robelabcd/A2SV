class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        left, right = 0, len(s) - 1
        
        def helper(left, right):
            if left > right:
                return ''

            look_up = {s[i] for i in range(left, right + 1)}
            
            for i in range(left, right + 1):
                char = s[i]
                if char.swapcase() not in look_up:
                    s1 = helper(left, i - 1)
                    s2 = helper(i + 1, right)

                    if len(s1) < len(s2):
                        return s2
                    return s1
            
            return s[left: right + 1]
        
        return helper(left, right)