class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        pos = 0
        while len(arr) > 1:
            rip = (pos + (k - 1)) % len(arr)
            arr.pop(rip)
            pos = rip

        return arr[0]
