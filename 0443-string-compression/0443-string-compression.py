class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
            ""
        '''
        i,j = 0,0

        while j<len(chars):

            count,letter = 0,chars[j]

            while j<len(chars) and chars[j]==letter:
                count +=1
                j +=1
            
            pos_let =[letter]
            
            if count > 1:
                pos_let += list(str(count))
            
            for k in range(len(pos_let)):
                chars[i] = pos_let[k]
                i +=1
        return i


            


