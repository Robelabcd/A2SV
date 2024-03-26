class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        forward_sum = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            forward_sum.append(temp)

        back_sum = []
        temp = 0
        for i in range(len(nums)-1, -1, -1):
            temp += nums[i]
            back_sum.append(temp)

        back_sum.reverse()


        for i in range(len(nums)):
            if forward_sum[i] == back_sum[i]:
                return i

        return -1
