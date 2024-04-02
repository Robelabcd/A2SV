class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        pref_sum = [0] * (len(nums)+1)
        pref_sum[0] = 0
        for i in range(1, len(pref_sum)):
            pref_sum[i] = pref_sum[i-1] + nums[i-1]
        print(pref_sum)
        # [0, -2, -1, -4, 0, -1, 1, 2, -3, 1]

        minn = inf
        min_arr = []
        for i in range(0, len(pref_sum)):
            minn = min(minn, pref_sum[i])
            min_arr.append(minn)
        print(min_arr)
        # [0, -2, -2, -4, -4, -4, -4, -4, -4, -4]

        maxx = -inf
        for i in range(1, len(pref_sum)):
            summ = pref_sum[i] - min_arr[i-1]

            maxx = max(summ, maxx)

        return maxx

        

        
        


            










