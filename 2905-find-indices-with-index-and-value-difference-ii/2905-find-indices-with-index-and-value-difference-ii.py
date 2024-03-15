class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
            #precompute minimum array backward
            n = len(nums)

            minback = []
            min_temp = nums[n-1]
            min_index = n-1
            for i in range(n-1, -1, -1):
                if min_temp > nums[i]:
                    min_temp = nums[i]
                    min_index = i
                minback.append(min_index)

            minback.reverse()
                
            
            max_temp = nums[0]
            for i in range(n -  indexDifference):

                max_temp = max(nums[i], max_temp)

                curr = i + indexDifference

                if (max_temp - nums[minback[curr]]) >= valueDifference:

                        return [i, minback[curr]]

            maxback = []
            max_temp = nums[n-1]
            max_index = n-1
            for i in range(n-1, -1, -1):
                if max_temp < nums[i]:
                    max_temp = nums[i]
                    max_index = i
                maxback.append(max_index)

            maxback.reverse()  
            
            min_temp = nums[0]
            for i in range(n -  indexDifference):

                min_temp = min(nums[i], min_temp)

                curr = i + indexDifference

                if abs(min_temp - nums[maxback[curr]]) >= valueDifference:

                        return [i, maxback[curr]]


            return [-1, -1]





























# another approach but time limit exceeded
        # for i in range(len(nums)):

        #     j = i + indexDifference

        #     if j == len(nums)-1:
        #         minn, maxx = nums[j], nums[j]
        #         min_ind, max_ind = j, j
            
        #     if j >= len(nums):
        #         break
            
        #     else:

        #         # minn = min(nums[j:])
        #         # min_ind = nums.index(minn, j)
        #         # maxx = max(nums[j:])
        #         # max_ind = nums.index(maxx, j)


        #     if abs(nums[i] - nums[min_ind]) >= valueDifference:
        #         return [i, min_ind]

        #     if abs(nums[i] - nums[max_ind]) >= valueDifference:
        #         return [i, max_ind]

        # return [-1, -1]






        #Brute force approach but time limit exceeded
        # i = 0
        # while i < len(nums)-indexDifference:

        #     j = i + indexDifference
        #     while j < len(nums):

        #         if (j - i) >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:

        #             return [i, j]

        #         j += 1
            
        #     i += 1

        # return [-1, -1]
