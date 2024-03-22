class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        lp = 0
        count = 0
        product = 1

        if k <= 0:

            return 0

        for rp in range(len(nums)):

            product *= nums[rp]

            while product >= k and lp < rp:
                product /= nums[lp]
                lp += 1

            if product == 1 and k == 1:
                continue

            count += rp - lp + 1

        return count