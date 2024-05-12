class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        '''
        [1,2,3,4,5,6,7,8,9,10].  day = 5

        low = minimum_weight = 10
        high = max_weight = sum(weights) = 55


        mid ->

        
        
        '''

        low, high = max(weights), sum(weights)

        while low <= high:

            mid = low + (high - low) // 2

            if self.isPossible(weights, mid, days):
                cap = mid 
                high = mid - 1
            else:
                low = mid + 1
            
        return cap

    '''
    low = 10, high=55 , mid = 55 + 10 // 2
    
    mid = 32

    isPossible([1,2,3,4,5,6,7,8,9,10],  cap = 32,  5 )

    
    
    '''



    def isPossible(self, weights, cap, days):
        current_capacity, count_day = 0, 1

        for x in weights:

            if current_capacity + x > cap:

                count_day += 1
                current_capacity = 0

            
            current_capacity += x


        return count_day <= days










