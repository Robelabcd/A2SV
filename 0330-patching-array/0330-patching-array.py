class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        n_ = len(nums)
        maxx = 0
        patches = 0
        i = 0
        while(maxx < n):
            if i < n_ and maxx+1 >= nums[i]:
                maxx += nums[i]
                i+=1
            else:
                patches += 1
                maxx += maxx+1
        return patches