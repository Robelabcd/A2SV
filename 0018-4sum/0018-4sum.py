class Solution(object):
    def fourSum(self, nums, target):

        nums.sort()
        quadruplets = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k = j + 1
                l = len(nums) - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        quadruplets.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1

        return list(quadruplets)        












#my first approach with some errors while doing(needs revision)
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

#         res = []
#         nums.sort()  

#         for i in range(len(nums)-3):
            
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue

#             for j in range(i+1, len(nums)-2):
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
            
#                 k, l = j + 1, len(nums) - 1

#                 while k < l:
#                     total_sum = nums[i] + nums[j] + nums[k] + nums[l]

#                     if total_sum == target:
#                         res.append([nums[i], nums[j], nums[k], nums[l]])
                    
#                         while k < l and nums[k] == nums[k+1]:
#                             j += 1
                    
#                         while k < l and nums[l] == nums[l-1]:
#                             l -= 1
#                         k += 1
#                         l -= 1
#                     elif total_sum < target:
#                         k += 1
#                     else:
#                         l -= 1

#         return res