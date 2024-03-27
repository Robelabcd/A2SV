class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = 1
        is_zero = 0
        for i in range(len(nums)):

            if nums[i] == 0:
                is_zero += 1
                continue

            prefix_product *= nums[i]

        edge = []
        if is_zero == 1 and len(nums) == 2:
            edge.append(nums[1])
            edge.append(nums[0])
            return edge    

        if is_zero == len(nums) or is_zero == len(nums)-1:
            return [0] * len(nums)       

        answer = []
        for i in range(len(nums)):

            if is_zero:

                if nums[i] == 0 and is_zero == 1:
                    answer.append(prefix_product)

                else:
                    answer.append(0)

            else:

                answer.append(prefix_product // nums[i])

        
        return answer
