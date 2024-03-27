class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        '''
        [1, 1, 1]  k = 2
        create hashmap for each prefix sum while calculating the the possible values

        prefix sums:
        1  -> 1 - k = -1 not possible but update dictt[1] by 1
        2  -> 2 - k = 0 possible although there is no zero, so initialize with {0:1}. And dictt[2]=1
        3  -> 3 - k = 1 possible since dictt[1] is there. And, update dictt[3] by 1

        all possibles = 2

        '''
        dictt = {0:1}
        prefix_sum = 0
        answer = 0
        i = 0
        while i < len(nums):

            prefix_sum += nums[i]
            required_prefixSum = prefix_sum - k

            answer += dictt.get(required_prefixSum, 0)
            dictt[prefix_sum] = dictt.get(prefix_sum, 0) + 1

            i += 1
        return answer