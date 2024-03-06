class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        for i in nums:
            temp_count, j = 0, 0
            while j < len(nums):

                if i > nums[j]:
                    temp_count +=1
                j += 1
            count.append(temp_count)

        return count