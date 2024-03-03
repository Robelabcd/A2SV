class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        i = len(arr)-1
        while i>=0:
            store = arr[i]
            arr[i] = greatest
            if store > greatest:
                greatest = store
            i-=1
        return arr











#approach 2 but time limit exceeded
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         res = []
#         temp = arr

#         if len(arr) == 1:
#             res.append(-1)
#             return res

#         for i in range(len(arr)-1):
            
#             temp.pop(0)
#             max_num = max(temp)
#             res.append(max_num)
            
#         res.append(-1)
#         return res