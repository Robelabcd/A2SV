# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         nums = sorted(people)
#         res = []

#         i, j = len(nums)-2, len(nums)-1
        
#         while i > 0:
            
#             if nums[j] >= limit:
#                 res.append([j])
#                 j -= 1
#                 i -= 1

#             else: 
#                 if nums[j] + nums[i] <= limit:
#                     res.append([i, j])
#                     i -= 2
#                     j -= 2
#                 while i > 0 and nums[j] + nums[i] > limit:
#                     i -= 1

#                 if i >= 0:  # Avoid accessing nums[j] when i < 0
#                     res.append(nums[j])
#                 j-=1
#                 i = j-1
                
#         return len(res)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1

        return boats

                

                






