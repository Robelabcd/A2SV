class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False

        max_num = max(arr)
        mid_index = arr.index(max_num)

        if mid_index == len(arr)-1 or mid_index == 0:
            return False

        for i in range(0, mid_index):
            if arr[i] >= arr[i+1]:
                return False

        for i in range(mid_index, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False


        return True
