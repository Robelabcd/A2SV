class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newstr = ''

        for i in s:

            if i.isalnum():

                newstr += i.lower()

        i, j = 0, len(newstr)-1

        while i < len(newstr):

            if newstr[i] == newstr[j]:
                i += 1
                j -= 1
            else: 
                return False

        return True