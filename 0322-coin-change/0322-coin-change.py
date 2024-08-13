class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0


        for i in range(1, amount+1):

            new_amount = i
            minn = amount+1
            for num in coins:

                if new_amount - num < 0:
                    continue

                if new_amount - num >= 0:
                    dp[new_amount] = 1 + dp[new_amount - num]
                    minn = min(minn, dp[new_amount])


            dp[new_amount] = minn

        # print(dp)
        return dp[amount] if dp[amount] <= amount else -1 
                
