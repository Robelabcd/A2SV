class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = 0    #index of words
        i = j = 0      #index of characters

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False
            i, j = i+1, j+1   
        
            if i == len(word1[w1]): #if the index of the character reaches the last character
                w1 += 1             #of the first word in the list
                i = 0    #since we need to start from the first index of the second word

            if j == len(word2[w2]):
                w2 += 1
                j = 0

        if w1 != len(word1) or w2 != len(word2):
            return False      #means it doesn't finish the whole iteration
        return True
        
        