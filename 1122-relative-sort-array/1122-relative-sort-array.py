class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        dictt = Counter(arr1)
        # keys = list(dictt1.keys())
        # keys.sort()
        # dictt = {i:dictt1[i] for i in keys}
    
        res = []

        for num in arr2:

            count = dictt[num]
            temp = [num] * count
            res.extend(temp)
            dictt[num] = 0

        
        for num in arr1:
            if dictt[num] != 0:
                count = dictt[num]
                temp = [num] * count
                res.extend(temp)
                dictt[num] = 0

        return res






