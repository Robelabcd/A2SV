import random

class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.idxmap = {}

    def insert(self, val):
        if str(val) in self.idxmap:
            return False
        else:
            self.arr.append(val)
            self.idxmap[str(val)] = len(self.arr) - 1
            return True

    def remove(self, val):
        if str(val) in self.idxmap:
            idx = self.idxmap[str(val)]
            last_val = self.arr[-1]
            self.arr[idx] = last_val
            self.idxmap[str(last_val)] = idx
            self.arr.pop()
            del self.idxmap[str(val)]
            return True
        else:
            return False

    def getRandom(self):
        return random.choice(self.arr)

        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()