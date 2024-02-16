class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        N = len(nums)

        for i in range(N+1):
            if not(i in nums):
                return i
        