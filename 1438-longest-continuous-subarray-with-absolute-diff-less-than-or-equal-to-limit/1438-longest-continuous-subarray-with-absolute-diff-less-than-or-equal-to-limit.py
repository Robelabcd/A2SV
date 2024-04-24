class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        inc = deque() 
        dec = deque()

        left = 0
        res = 0

        for i, val in enumerate(nums):

            while inc and nums[inc[-1]]<val:
                inc.pop()

            inc.append(i)

            '''
            2
            
            
            '''

            while dec and nums[dec[-1]] > val:

                dec.pop()

            dec.append(i)

            '''
            1 2
            
            '''
            while nums[inc[0]] - nums[dec[0]] > limit:

                if inc[0] == left:
                    inc.popleft()

                if dec[0] == left:
                    dec.popleft()

                left += 1

            res = max(res, i - left + 1)


        return res

