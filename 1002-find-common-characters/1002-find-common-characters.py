class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        w = Counter(words[0])
        n = len(words)
        
        for i in range(1, n):
            t = Counter(words[i])
            w = w & t
        
        ans = []
        for k in w.keys():
            for i in range(w[k]):
                ans.append(k)
        
        return ans
        