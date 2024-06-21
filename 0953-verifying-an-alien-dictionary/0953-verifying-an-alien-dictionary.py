class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # {letter -> index}  to compare their order

        index_order = {c : i for i, c in enumerate(order)}


        #Traverse through 'words' and compare
        '''
        words = ["hi", "hello"]

        1 comparison is enough, so up to -> len(words) - 1
        '''
        for i in range(len(words)-1):

            word_1, word_2 = words[i], words[i+1]

            #compare the order of each letter

            for j in range(len(word_1)):

                #if j reach len(word_2), no way word_1 is smaller than word_2
                if j == len(word_2):
                    return False

                #compare the index - lexographically correct order
                if word_1[j] != word_2[j]:
                    if index_order[word_1[j]] >= index_order[word_2[j]]:
                        return False
                    
                    break  #it's different and correct order - so no need to proceed with rest of the letters
        
        return True