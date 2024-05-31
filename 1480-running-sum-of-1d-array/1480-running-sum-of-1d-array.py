class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #practice
        running_sum = 0
        out_put = []

        for i in range(len(nums)):

            running_sum += nums[i]
            out_put.append(running_sum)

        return out_put  