class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        n=len(nums)
        dp=[[-1 for j in range(n+1)] for i in range(n)]
        
        def backtrack(index,previous):
            
            if index==n:
                return 0
            
            if dp[index][previous+1]!=-1:
                return dp[index][previous+1]
            
            
            not_take=0+backtrack(index+1,previous)
            
            take=0
            if previous==-1 or nums[index]>nums[previous]:
                take=1+backtrack(index+1,index)
            
            dp[index][previous+1]=max(take,not_take)
            
            return dp[index][previous+1]
        
        
        return backtrack(0,-1) 

        '''
        
        #bottom up approach
        
        n=len(nums)
        dp=[[0 for j in range(n+1)] for i in range(n+1)]
        
        for index in range(n-1,-1,-1):
            for previous in range(index-1,-2,-1): 
                
                not_take=0+dp[index+1][previous+1]
                
                take=0
                if previous==-1 or nums[index]>nums[previous]:
                    take=1+dp[index+1][index+1]
                
                dp[index][previous+1]=max(take,not_take)
        
        return dp[0][0]  