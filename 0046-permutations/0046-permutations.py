class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        '''
        [1, 2, 3]

        without 1, without 2, without 3
        breaking down problems: 3-->2--1
        
        base case: if len(nums) = 1, return the list - nums itself
        '''

        all_per = []

        #base case
        if len(nums)==1:
            return [nums[:]]

        for i in range(len(nums)):
            #pop the first element [1, 2, 3] ---> [2, 3] ---> [3]
            first = nums.pop(0)

            #recursion to reach base
            divided_perm = self.permute(nums)

            for each_list in divided_perm:
                each_list.append(first)

            all_per.extend(divided_perm)
            nums.append(first)

        return all_per










