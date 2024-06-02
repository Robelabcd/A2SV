class Solution:



    def reverse(self, initial, end, s):

        #base case
        if initial >= end:
            return

        s[initial], s[end] = s[end], s[initial]

        self.reverse(initial+1, end - 1, s)




    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # n = len(s)

        # for i in range(n//2):

        #     s[i], s[n-i-1] = s[n-i-1], s[i]

        # Recurssion

        n = len(s)
        end = n - 1
        # i = 0 --> initial

        self.reverse(0, end, s)




