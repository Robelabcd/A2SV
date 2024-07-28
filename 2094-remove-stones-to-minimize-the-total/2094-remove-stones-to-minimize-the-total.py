class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        
        #bruteforce approach

        # - find max_ each time:
            # divide by two - k times

        # - add all the nums and return
        '''
        for _ in range(k):

            maxx = max(piles)

            index = piles.index(maxx)

            piles[index] = piles[index] - piles[index]//2

        
        return sum(piles)

        Time complexity: O(k*n)
        '''
        res = sum(piles)
        heapp = []
        for x in piles:
            heapq.heappush(heapp, -x)

        for _ in range(k):
            maxx = heapq.heappop(heapp)
            reduced = math.floor(-maxx / 2)
            res -= reduced
            heapq.heappush(heapp, maxx + reduced)

        return res
