class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        '''
        [8,15,10,20,8], k = 2

        distribution :  ___ ___ for two kids
                   8,0          0,8
                
                23,0   0,15    15,8   0,23
            ......and so on 
    
        max_dis = max(__,__)

        min_unfairness = min(min_unfairness, max_dist)
        '''

        min_unfair = inf  
        dist = [0] * k    #meaning: for k = 2 ---> [___ , ___] intially both are zero

        def helper(index):   #backtracking function

            nonlocal min_unfair, dist   #nonlocal -> to use global variables inside nested function

            #base case: if it reaches the len(cookies), that means we can calculate
            #max_dist and min_unfairness
            if index == len(cookies):
                min_unfair = min(min_unfair, max(dist))
                return

            if min_unfair <= max(dist):
                return


            #now the main operation 
            for j in range(k):
                '''
                for k = 2, we only have two branches--> so j=0 and j=1
                              ---i.e 8,0 or 0,8
                              and so on
                starting from index = 0 ---> 8
                do the backtrack by adding and removing the values, 
                and the min_unfair will be updated along the way
                '''
                dist[j] += cookies[index]
                helper(index+1)
                dist[j] -= cookies[index]


        
        #call the helper function by starting from index = 0
        helper(0)

        return min_unfair












