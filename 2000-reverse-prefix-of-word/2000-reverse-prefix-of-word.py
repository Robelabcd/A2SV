class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        temp = ""
        count = 0
        for i in word:

            temp += i

            if i == ch and count == 0:
                temp = temp[len(temp)-1::-1]
                count += 1

            
        return temp
