class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def helper(left, right, s):

            if left >= right:
                return 

            s[left], s[right] = s[right], s[left]

            helper(left+1, right-1, s)

        
        helper(0, len(s)-1, s)