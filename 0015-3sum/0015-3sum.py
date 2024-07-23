class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  

        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif total_sum < 0:
                    j += 1
                else:
                    k -= 1

        return res


# #class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         for i in range(len(nums)-2):
            
#             j, k = i + 1, i + 2
#             while k < len(nums):

#                 if (nums[i] + nums[j] + nums[k]) == 0:
#                     res.append([nums[i], nums[j], nums[k]])

#                 j += 1
#                 k += 1

#         for i in range(len(res)-1, -1, -1):
#             print(res[i])

#         return res


