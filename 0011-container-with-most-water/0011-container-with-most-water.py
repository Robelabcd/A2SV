class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height)-1
        

        max_area = 0
        while i < j:  
            temp_height = min(height[i], height[j])
            temp_width = j - i
            temp_area = temp_height * temp_width


            max_area = max(temp_area, max_area)

            if height[i] > height[j]:
                j -= 1
            else: 
                i += 1

        return max_area
