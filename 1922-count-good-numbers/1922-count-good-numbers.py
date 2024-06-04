class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        res = 1
        for i in range(n):
            if i%2 == 0:
                res = res * 5

            else:
                res = res * 4

        return (res)%mod