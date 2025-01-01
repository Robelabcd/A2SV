class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dictt = {}   
        for i in nums:
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1
        
        for i in dictt:
            if dictt[i] > 1:
                return True

        return False

