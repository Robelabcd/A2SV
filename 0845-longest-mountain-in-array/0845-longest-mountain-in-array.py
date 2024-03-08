class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        if len(arr) < 3:
            return 0
        
        top_mountain = 1
        length_mountain = 0
        while top_mountain < len(arr)-1:
            left = top_mountain
            while left > 0 and arr[left] > arr[left -1]:
                left -= 1
            
            right = top_mountain
            while right < len(arr) -1 and arr[right] > arr[right + 1]:
                right += 1
            
            if (left - top_mountain) == 0 or (right - top_mountain) == 0:
                top_mountain = right + 1
                continue
            
            top_mountain = right + 1
            
            d = (right - left) + 1
            if d > length_mountain:
                length_mountain = d
        
        return length_mountain