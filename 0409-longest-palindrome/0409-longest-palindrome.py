class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dictt = Counter(s)
        print(dictt)

        
        res = 0

        for i in dictt:

            print(dictt[i])
            num = dictt[i]//2

            res += num


        return (res*2) if (res*2) == len(s) else (res*2)+1

