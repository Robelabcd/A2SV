class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        return self.checkPalindrome(a, b) or self.checkPalindrome(b, a)


    def checkPalindrome(self, a: str, b: str) -> bool:
        
        def palindrome(s):
            i, j = 0, len(s)-1
            while i < len(s) and j > -1:
    
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False

            return True
        
        i, j = 0, len(a) - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        check1 = a[i:j + 1]
        check2 = b[i:j + 1]

        
        if palindrome(check1) or palindrome(check2):
            return True
        return False