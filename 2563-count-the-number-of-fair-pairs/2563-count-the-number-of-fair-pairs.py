class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        

        def _count(a):
            l, r = 0, len(nums) - 1
            total = 0
            while l < r:
                if nums[l] + nums[r] > a:
                    r -= 1
                else:
                    total += r - l
                    l += 1
            return total

        
        count_up = _count(upper)
        
        
        count_low = _count(lower - 1)
        
        
        return count_up - count_low