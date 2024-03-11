class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        #now i hold the first element to be swapped
        
        if i >= 0:
 
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the subarray to the right of nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


        
