class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]


        for i in range(2, n+1):
            cur_cost = 0
            if i < n:
                cur_cost = cost[i]
        

            dp[i] = cur_cost + min(dp[i-2], dp[i-1])

        return dp[n]