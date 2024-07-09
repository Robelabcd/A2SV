class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        combinations = []

        def backtrack(index=0, comb=[]):
            
            if target == sum(comb):
                combinations.append(comb[:])
                return 

            if target < sum(comb):
                return 

            for i in range(index, n):
                comb.append(candidates[i])
                backtrack(i, comb)
                comb.pop()
        
        backtrack()
        
        return combinations     