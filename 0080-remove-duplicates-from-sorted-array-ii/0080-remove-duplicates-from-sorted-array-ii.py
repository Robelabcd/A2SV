class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, j = 0, 1
        
        while j < len(nums):
            count = 0
            while j < len(nums) and nums[i] == nums[j]:
                count += 1
                if count >= 2:
                    nums.pop(j)
                else:
                    j += 1
            if count <= 1:
                i = j
                j += 1
        return len(nums)

