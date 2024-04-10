class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
        '''
        target = 4  [1, 1, 1, 2, 3]
        [1, 1, 1, 2, 3, 1, 1, 1, 2, 3]    2*nums since it's possible to add 3+1 respectively

        at first, dicts = {0:-1}

        running_sum = 1
        needed = rs - target = 1 - 4 = -3 however -3 is not in dictt
        {1: 0}  ----> {prefix_sum : index}

        rs = 2
        n = 2 - 4 = -2 nope!
        {1:0, 2:1}

        rs = 3
        n = 3 - 4 = -1 nope!
        {1:0, 2:1, 3:2}

        rs = 5
        n = 5 - 4 = 1  yes!
        result = min(result, i - dicts[n])
        {1:0, 2:1, 3:2, 5:3}
         
        

        edge case: what if tartget is more than the sum of nums


        window_size, target = divmod(target, sum(nums))

        if target=0: N * window_size
        
        '''
        
        window_size, target = divmod(target, sum(nums))

        if target == 0: return len(nums) * window_size


        res = inf
        dicts = {0:-1}
        run_sum = 0

        for i, val in enumerate(nums*2):

            run_sum += val

            needed = run_sum - target

            if needed in dicts:
                res = min(res, i - dicts[needed])

            dicts[run_sum] = i


        return -1 if res == inf else len(nums)*window_size + res























