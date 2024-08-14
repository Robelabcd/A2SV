class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        res, sol = {}, 0

        
        def backtrack(i, sol):

            if i == len(nums):
                if sol == target:
                    return 1
                return 0

            if (i, sol) in res:
                return res[(i, sol)]

            
            res[(i, sol)] = backtrack(i+1, sol + nums[i]) + backtrack(i+1, sol - nums[i])
        
            return res[(i, sol)]


        return backtrack(0, sol)