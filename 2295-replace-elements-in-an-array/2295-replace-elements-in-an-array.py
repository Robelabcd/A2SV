class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_index = {num: i for i, num in enumerate(nums)}
        result = [0] * len(nums)

        for key, val in operations:
            index = nums_index[key]
            nums_index[key] = len(nums)
            nums_index[val] = index

        for key, val in nums_index.items():
            if val < len(result):
                result[val] = key

        return result