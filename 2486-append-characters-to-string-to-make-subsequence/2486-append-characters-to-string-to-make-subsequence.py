class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        def helper(ind_s, ind_t):

            if ind_t == len(t):
                return 0

            if ind_s == len(s):
                return len(t) - ind_t

            if s[ind_s] == t[ind_t]:

                return helper(ind_s + 1, ind_t + 1)

            return helper(ind_s + 1, ind_t)

        
        return helper(0, 0)