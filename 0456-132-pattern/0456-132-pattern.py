class Solution:
    def find132pattern(self, nums: List[int]) -> bool:


        mini = [nums[0]]
        temp = nums[0]
        for i in range(len(nums)):
            temp = min(temp, nums[i])
            mini.append(temp)

        

        for i in range(1, len(nums)):

            if nums[i] < nums[i-1]:
                if mini[i-1] < nums[i]:
                    return True

        return False 

































        
        '''
        small --> big ---> medium 132 pattern

        queue = deque() 

        1 -popleft      2 - 3 - but 4. so no 132 pattern


        3 -pop   1 - 4 - 2 possible


        what if we have to jump an in-between element?
        e.g  [-1,3,2,0]  -1 --> 2 ---> 0. possible  how to avoid 3 in this case?
        
        '''

        # small = []
        # temp = nums[-1]
        # for i in range(len(nums)-1, -1, -1):

        #     if temp > nums[i]:
        #         temp = nums[i]

        #     small.append(temp)

        # small.reverse()


        # stack = []
        # j = 0

        # for i in range(len(nums)-2):

        #     stack.append(nums[i])
        #     if len(stack) == 2:

        #         if nums[i+1] > stack[j]:
                    
        #             if stack[i] < small[i] < nums[j+1]:
        #                 return True

        #         else:
        #             j += 1


        # return False            



    



















            
