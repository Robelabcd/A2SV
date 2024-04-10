class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        '''
        [ 3, 4, 1, 2] k = 25

        [3, 7, 8, 10]   k%10 = 5

        7 > 5 so index 1 will replace the chalk
    
        '''

        prefix = [0]*len(chalk)
        prefix[0] = chalk[0]
        for i in range(1, len(chalk)):
            prefix[i] = prefix[i-1] + chalk[i]

        val = k % prefix[-1]

        for i in range(len(prefix)):
            if val < prefix[i]:
                return i
