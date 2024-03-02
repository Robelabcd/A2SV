# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
        
#         str1 = list(words[0])      #assume str1 contains the duplicate 

#         for i in range(1, len(words)):
#             str2 = words[i]       #stores the next word each time
#             for x in str1:
#                 if not(x in str2):
#                     str1.remove(x)

        


#         return str1
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_word = []
        first_word = words[0]
        
        for char in set(first_word):
            count = first_word.count(char)
            for word in words[1:]:
                count = min(count, word.count(char))
            
            common_word.extend([char] * count)

        return common_word