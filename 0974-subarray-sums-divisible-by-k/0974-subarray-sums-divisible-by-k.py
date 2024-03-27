class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        #Same way as Subarray Sums equals k
        '''
        [4, 9, 9,  7,  4, 5]    k = 5

        [4, 5, 0, -2, -3, 1]

        prefix_sums:
        4 -> 4 % 5 = 4
        9 -> 9 % 5 = 4
        9 -> 9 % 5 = 4
        7 -> 7 % 5 = 2
        4 -> 4 % 5 = 4
        5 -> 5 % 5 = 0
        '''
        
        dictt = {0:1}

        prefix_sum = 0

        answer = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            modulo = prefix_sum % k
            answer += dictt.get(modulo, 0)

            dictt[modulo] = 1 + dictt.get(modulo, 0)

        return answer


        
