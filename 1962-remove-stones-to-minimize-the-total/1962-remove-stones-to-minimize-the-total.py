class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
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
     