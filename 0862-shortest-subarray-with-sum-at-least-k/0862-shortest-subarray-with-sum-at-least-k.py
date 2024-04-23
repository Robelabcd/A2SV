# from collections import deque  --->not needed this time but to use deque we need this
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        '''
        [17,85,93,-45,-21]--> nums and k = 150

        17 + 85 + 93 >= 150  res = 3 --> store the index in deque to make the removal
                                         of the first element easier

             85 + 93 >= 150  res = min(3, 2) =2
        
        Note: do the prefix sum instead of adding each time
        '''
        n = len(nums) #to make it easier for later use

        #pre-compute the sum instead of adding each time --> to save time
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        #create deque to store the indices so that to know the distance
        deque_index = deque()
        res = float('inf') #since we take the minimum value

        for i in range(n + 1):
            
            #sum >= k --> popleft
            while deque_index and prefix_sum[i] - prefix_sum[deque_index[0]] >= k:
                res = min(res, i - deque_index.popleft())
            
            
            while deque_index and prefix_sum[i] <= prefix_sum[deque_index[-1]]:
                deque_index.pop()

            deque_index.append(i)

        return res if res != float('inf') else -1
