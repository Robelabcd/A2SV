class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        sorted_arr = sorted(arr)

        maxx = 0
        for num in sorted_arr:

            if num > maxx + 1:
                num = maxx + 1
            
            maxx = num
        
        return maxx