class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        '''
        [8,-19,5,-4,20]
                

        '''

        
        lp, rp = 0, 0
        summ = 0
        res = max(nums)
        for rp in range(len(nums)):
            summ += nums[rp]
            if summ <= nums[rp]:
                
                lp = rp

                summ = nums[lp]

            res = max(res, summ)

        

        return res











