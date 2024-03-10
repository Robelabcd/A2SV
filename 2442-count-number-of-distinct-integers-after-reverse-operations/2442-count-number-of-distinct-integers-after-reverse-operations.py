class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set(nums)
        for number in nums:
            res.add(int(str(number)[::-1]))
        
        return len(res)
        











        #will come back to this later
        # n = len(nums)

        # for i in range(n):

        #     strr = str(nums[i])
        #     strr1 = strr[::-1]
        #     strr2 = int(strr1)
            
        #     nums.append(strr2)
        # i, j = 0, 1
        # while i < len(nums):

        #     while i < len(nums) and nums[i] == nums[j]:

        #         j += 1

        #     count += 1
        #     i += 1
        #     j += 1
        # return count
