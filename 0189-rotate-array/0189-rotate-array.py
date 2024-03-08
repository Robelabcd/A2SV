class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        n = len(nums)
        k = k % n  

        
        numss = [val for val in nums]

        
        for i in range(n):
            nums[i] = numss[(i - k) % n]
       
       
       
       
       
       
       
       
       
         
       #other approach with some problems(come back to it if you have time)
       
       
        # arr1 = []
        # arr2 = []
        # numss = [val for val in nums]

        # '''
        #     [-1,-100,3,99].  k=2
        #     target = 3
            
        # '''
        # target =  len(nums) - k
        # print(k % len(nums))
        # for i in range(0, len(numss)-k, 1):
            
        #     nums[-target]= numss[i]
        #     target -= 1
     
        # a = 0
        # j = len(nums) - k
        # #for j in range(len(numss)-k, len(numss), 1):   #4, 5, 6
        # while a < k and j < len(nums):
        #     nums[a] = numss[j]
        #     a += 1
        #     j += 1



    
        # a, b = 0, 0
        # while a < len(nums):
        #     if a >= len(arr1):
        #         nums[a] = arr2[b]
        #         b += 1
        #     nums[a] = arr1[a]