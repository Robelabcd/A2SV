class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        ptr1 = ptr2 = 0

        while ptr1 < len(s) and ptr2 < len(t):

            if s[ptr1] == t[ptr2]:
                ptr2 += 1

            ptr1 += 1


        return len(t) - ptr2