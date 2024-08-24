class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev, cur = 0, 0

        for n in nums:
            newRob = max(prev + n, cur)
            prev = cur
            cur = newRob
        return cur
