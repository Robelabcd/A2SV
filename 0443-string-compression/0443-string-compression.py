class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
            ["a","a","b","b","c","c","c"] to ["a","2","b","2","c","3"]
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
            
            for x in range(len(pos_let)):
                chars[i] = pos_let[x]
                i +=1
        return i


            


