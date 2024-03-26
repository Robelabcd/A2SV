class NumArray:

    def __init__(self, nums: List[int]):

        self.prefixSum = []
        temp = 0

        for i in range(len(nums)):
            temp += nums[i]
            self.prefixSum.append(temp)
        

    def sumRange(self, left: int, right: int) -> int:

        #since we want to remove the values before the left side
        left_side = self.prefixSum[left - 1] if left > 0 else 0  
        right_side = self.prefixSum[right]


        return right_side - left_side

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)