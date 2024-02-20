class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ls1=set("qwertyuiop")
        ls2=set("asdfghjkl")
        ls3=set("zxcvbnm")
        res=[]
        for k in words:
            w=k.lower()
            w=list(w)
            for i in w:
                if not(i in ls1):
                    break
            else:
                res.append(k)
            for i in w:
                if not(i in ls2):
                    break
            else:
                res.append(k)
            for i in w:
                if not(i in ls3):
                    break
            else:
                res.append(k)
        return res