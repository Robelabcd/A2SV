class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backtrack(first_num, comb):
            
            if len(comb) == k:
                res.append(comb[:])
                return

            for num in range(first_num, n+1):
                comb.append(num)
                backtrack(num+1, comb)
                comb.pop()

        
        backtrack(1,[])
        return res