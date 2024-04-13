class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        row, col = len(matrix), len(matrix[0])
        histogram = [0] * col
        max_area = 0
        
        for r in range(row):
            for c in range(col):
                histogram[c] = histogram[c] + 1 if matrix[r][c] == '1' else 0
            
            max_area = max(max_area, self.largestRectangleArea(histogram))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
