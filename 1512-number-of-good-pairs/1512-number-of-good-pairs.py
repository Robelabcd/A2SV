class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {} 
        for i in range(0, len(nums)): 
            if (nums[i] in dict): 
                dict[nums[i]] += 1
            else: 
                dict[nums[i]] = 1
            # initialize result 
            res = 0
        for key in dict: 
            if (dict[key] >= 2): 
                res += ((dict[key] * (dict[key] - 1)) // 2) 
        return res
        