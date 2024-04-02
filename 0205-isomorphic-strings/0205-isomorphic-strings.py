from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        
        dictt = Counter(s)
        dictt2 = Counter(t)

        for i in range(len(s)):

            if dictt[s[i]] != dictt2[t[i]]:
                return False

        dictt3 = {}

        for i in range(len(s)):
            
            val_s = dictt3.get(s[i], t[i])

            if val_s != t[i]:
                return False
            
            dictt3[s[i]] = val_s


        return True
















        
