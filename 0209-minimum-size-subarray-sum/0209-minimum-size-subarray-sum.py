class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        lp, summ = 0, 0
        res = float("inf")     #since we want the minimum value afterwards

        for rp in range(len(nums)):

            summ += nums[rp]

            while summ >= target:

                res = min((rp-lp+1), res)  #rp - lp + 1 is the current length

                summ -= nums[lp]  #reducing the value before updating the left pointer

                lp += 1


        if res == float("inf"):
            return 0

        else:
            return res

