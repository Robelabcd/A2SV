class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_array = sorted(nums) 
        count = []
        for i in nums:
            count.append(sorted_array.index(i))
        return count