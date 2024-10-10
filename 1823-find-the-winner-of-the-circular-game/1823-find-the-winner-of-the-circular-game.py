class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        n = 5, k = 2
        
        [1, 2, 3, 4, 5] 
        [1, 3, 4, 5]
        [1, 3, 5]
        [1, 3, 5]
        [3, 5]
        [3] ----> winner

        '''

        players = [i for i in range(1, n+1)]

        ptr = 0
        while len(players) > 1: # [1, 3] k = 5 ptr=1
            ptr += (k-1) 

            if ptr >= len(players):
                ptr = (ptr%len(players))

            players.pop(ptr)

            if ptr >= len(players):
                ptr = (ptr%len(players))


        return players[0] 
