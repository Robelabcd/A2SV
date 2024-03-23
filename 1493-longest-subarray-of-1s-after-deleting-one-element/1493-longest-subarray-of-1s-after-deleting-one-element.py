class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        count_zeros = 0
        lp = 0

        for rp in range(len(nums)):
            if nums[rp] == 0:
                count_zeros += 1

            while count_zeros > 1:
                if nums[lp] == 0:
                    count_zeros -= 1
                lp += 1

            max_length = max(max_length, rp - lp)

        return max_length


#Time complexity : O(n)
#Space Complexity : O(1)
