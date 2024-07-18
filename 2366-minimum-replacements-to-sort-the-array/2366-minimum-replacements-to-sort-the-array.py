class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        '''
        [3,9,3]

        [3,3,6,3] -1st
        
        [3, 3, 3, 3, 3] -2nd

        '''

        n = len(nums) 
        ops = 0
        end_ptr_num = nums[-1]

        for i in range(n - 2, -1, -1):
            cur_num = nums[i]

            if cur_num > end_ptr_num:
                remainder = cur_num % end_ptr_num
                
                if remainder == 0:

                    count_ops = cur_num // end_ptr_num
                    ops += count_ops - 1

                else:
                    count_ops = cur_num // end_ptr_num + 1
                    ops += count_ops - 1
                    end_ptr_num = cur_num // count_ops

            else:
                end_ptr_num = cur_num

        return ops