class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum = 0
        #nums.sort()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    sum +=1
        return sum
        
        