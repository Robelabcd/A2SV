class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.divide(nums, 0, n-1)
        return nums


    def divide(self, nums, l, r):
        if l < r:
            m = (l+r)//2

            self.divide(nums, l, m)
            self.divide(nums, m+1, r)

            self.merge(nums, l, m, r)

    def merge(self, nums, l, m, r):
        
        left_side = nums[l:l+(m-l+1)]
        right_side = nums[m+1:r+1]

        i, j = 0, 0
        index = l
        while i < (m-l+1) and j < (r-m):
            if left_side[i] <= right_side[j]:
                nums[index] = left_side[i]
                i+=1

            else:
                nums[index] = right_side[j]
                j+=1

            index += 1

        #leftovers

        while i < (m-l+1):
            nums[index] = left_side[i]
            index += 1
            i += 1

        while j < (r-m):
            nums[index] = right_side[j]
            j += 1
            index += 1





