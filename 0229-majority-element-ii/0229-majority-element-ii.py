class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        nums_count = Counter(nums)
        n = len(nums)
        occur = n // 3
        for key, val in nums_count.items():
            if val > occur:
                result.append(key)
        return result
