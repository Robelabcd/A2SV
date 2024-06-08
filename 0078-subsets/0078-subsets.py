class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        '''
        [1, 2, 3]  --->finding all the possible subsets
        
        Note: 
          [1, 2] and [2, 1] are the same since we're finding subset, not permutation


        Two possibility for each number: with or without

                                    {1}  or {}       --->with or without 1
                
                            {1, 2} or {1} ------ {2} or {}   --->with or without 2

            {1, 2, 3} or {1, 2}--{1,3} or {1}---{2,3} or {2}---{3} or {}  ---->with or without 3


        ---> we have 8 subsets
        
        *Now, this can be solved by backtracking

           i.e adding or removing the element and backtrack
        '''

        all_subset = []  #final answer

        each_subset = [] #to collect each subsets


        #backtracking function
        def helper(index):
            #base case: iterate all elements or len(nums)
            #and append each_subset to all_subset
            if index >= len(nums):
                all_subset.append(each_subset.copy())
                return

            
            #with or without decisions

            #with the element or nums[i]
            each_subset.append(nums[index])
            helper(index+1)

            #without the element
            each_subset.pop()
            helper(index+1)



        #start with index=0
        helper(0)



        return all_subset
            























