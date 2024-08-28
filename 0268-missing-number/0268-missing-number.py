class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        N = len(nums)
        num_set = set(nums)

        for i in range(N+1):
            if not(i in num_set):
                return i
        '''

        # maxx = max(nums)
        res = 0
        new_nums = nums
        for i in range(len(nums)+1):
            new_nums.append(i)

        print(nums)
        for num in new_nums:

            res = res ^ num

        return res