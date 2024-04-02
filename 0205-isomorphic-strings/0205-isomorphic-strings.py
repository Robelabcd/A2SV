from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        
        dictt = Counter(s)     #to check the frequency of that character
        dictt2 = Counter(t)

        for i in range(len(s)):

            if dictt[s[i]] != dictt2[t[i]]:
                return False

        dictt3 = {}             #to check the positions are not mismatched

        for i in range(len(s)):
            
            val_s = dictt3.get(s[i], t[i])

            if val_s != t[i]:
                return False
            
            dictt3[s[i]] = val_s


        return True



#Time complexity: O(n)
#Space complexity: O(1) 
'''Since the number of unique characters in a string is bounded (typically by the size of the character set, such as ASCII or Unicode)'''












        
