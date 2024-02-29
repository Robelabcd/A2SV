class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        def pancake_flip(k):
            arr[:k] = reversed(arr[:k])

        for i in range(len(arr), 0, -1):
            max_index = arr.index(max(arr[:i])) + 1
            if max_index != i:
                pancake_flip(max_index)
                result.append(max_index)
                pancake_flip(i)
                result.append(i)
    
        return result