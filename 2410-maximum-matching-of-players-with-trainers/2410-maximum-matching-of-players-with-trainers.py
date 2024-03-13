class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        

        players.sort()
        trainers.sort()

        count = 0

        i, j = 0, 0
        while i < len(players):

            while j < len(trainers):
                
                if players[i] <= trainers[j]:
                    count += 1
                    j += 1
                    break

                j += 1

            i += 1
        return count