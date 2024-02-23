class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            if nums[i] == 0:
                continue
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0 
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)

        # for i in range(0, count):
        #     nums.append(0)

        return nums

# nums = [1, 2, 3]
# print(len(nums))
# for i in range(0, len(nums)):
#     print(nums[i])