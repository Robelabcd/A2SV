from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        
        self.positive = set(list(range(1, 1001)))
        # heapify(self.positive)

    def popSmallest(self) -> int:
        mini = min(self.positive)

        self.positive.remove(mini)

        return mini

    def addBack(self, num: int) -> None:
        if num not in self.positive:
            self.positive.add(num)
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)