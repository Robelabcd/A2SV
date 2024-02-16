class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lose = {}
        for winner, loser in matches:
            if loser in lose:
                lose[loser] += 1
            else:
                lose[loser] = 1

            if winner in win:
                win[winner] += 1
            else:
                win[winner] = 1
                
        always_winners = [item for item in win if item not in lose]
        once_losers = [item for item in lose if lose[item] == 1]
        return [sorted(always_winners), sorted(once_losers)]