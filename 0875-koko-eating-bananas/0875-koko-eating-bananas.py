class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)

        while low <= high:

            mid = low + (high - low)//2

            if self.possible(piles, mid, h):

                result = mid
                
                high = mid -1

            else:

                low = mid + 1


        return result



    def possible(self, piles, k, hours):

        time = 0

        for each in piles:
            time += (each + (k-1))//k    #other way of finding the ceil value of time


        return time <= hours











