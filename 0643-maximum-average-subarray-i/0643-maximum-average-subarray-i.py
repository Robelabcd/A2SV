class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum = sum(nums[:k])

        maxa = window_sum / k

        for i in range(k, len(nums)):

            window_sum += nums[i] - nums[i-k]
            temp = window_sum / k

            maxa = max(maxa, temp)

        return maxa

