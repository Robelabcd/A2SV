class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        sign = 1 if num > 0 else -1
        num = abs(num)
        nums = []
        while num:
            num, mod = divmod(num, 10)
            nums.append(mod)
        
        nums.sort()
        n = len(nums)
        res = 0
        print(nums)
        if sign == -1:
            for i in range(n-1, -1, -1):
                res = res * 10 + nums[i]
            res *= -1
        else:
            i = 0
            while i < n and nums[i] == 0:
                i += 1
            nums[0], nums[i] = nums[i], nums[0]
            print(nums)
            for i in range(n):
                res = res * 10 + nums[i]
        
        return res


