from collections import Counter #codeforces
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicts_t = Counter(t)
        dicts_s = defaultdict(int)   #codeforces
        lp = 0
        res = []
        visited = 0
        start, end = 0, inf
        for rp in range(len(s)):
            
            dicts_s[s[rp]] += 1
            if dicts_s[s[rp]] == dicts_t[s[rp]]:
                visited += dicts_s[s[rp]]

            '''
            zyw ADOBEC ADEBANC.  
            t = {A:1, B:1, C:1}
            visited = 0

            zywADOBEC
            s - {A:2, B:1, C:1}.   visited = 3
            
            ADOBEC lp = 3 , rp = 8

            '''
            while lp <= rp and dicts_s[s[lp]] - 1 >= dicts_t[s[lp]] and visited == len(t):

                dicts_s[s[lp]] -= 1
                lp += 1

            if visited == len(t):

                if end - start > rp - lp:

                    start, end = lp, rp

            

        if end == inf:
            return ""
        else:
            return s[start:end+1]
