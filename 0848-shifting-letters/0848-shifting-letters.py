class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        
        prefix = []
        temp = 0
        for i in range(len(shifts)-1, -1, -1):
            temp += shifts[i]
            prefix.append(temp)

        prefix.reverse()

        alpa = "abcdefghijklmnopqrstuvwxyz"
        res = ""

        for i in range(len(s)):
            ind = (alpa.index(s[i]) + prefix[i]) % 26
            res = res + alpa[ind]
            
            
        return res


