class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        N = len(nums)
        num_set = set(nums)

        for i in range(N+1):
            if not(i in num_set):
                return i
        