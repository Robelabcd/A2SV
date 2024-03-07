class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()

        
        n = len(nums)
        pairs = [(nums[i], nums[n - i - 1]) for i in range(n // 2)]

        
        max_pair_sum = max(a + b for a, b in pairs)

        return max_pair_sum