class Solution:
    def reverseWords(self, s: str) -> str:
        
        #remove the unnecessary spaces
        res = " ".join(s.strip().split())
        
        list1 = list(res.split(" "))
        
        list1.reverse()

        return (" ".join(list1))

