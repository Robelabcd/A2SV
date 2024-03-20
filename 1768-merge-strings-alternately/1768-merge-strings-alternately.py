class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        j = 0
        k = 0
        while j < len(word1) and k < len(word2):
            merged += word1[j]
            merged += word2[k]
            j += 1
            k += 1
            
        merged += (word1[j:] + word2[k:])
        return merged