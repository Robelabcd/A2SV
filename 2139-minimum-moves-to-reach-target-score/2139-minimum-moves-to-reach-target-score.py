class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:


        '''
        149 2


        148
        74 1
        37 
        
        '''
        
        current = target
        count = 0

        while current > 1:
            
            if current % 2 == 0 and maxDoubles > 0:
                maxDoubles -= 1
                current = current // 2
                count += 1
            
            elif maxDoubles == 0:
                count += (current - 1)
                break 

            else:
                current = current - 1
                count += 1

        return count
            
            
