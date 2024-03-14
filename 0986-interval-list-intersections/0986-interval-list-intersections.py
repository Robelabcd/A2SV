class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        
        '''
        [[0,2],[5,10],[13,23],[24,25]]

        [[1,5],[8,12],[15,24],[25,26]]

        [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        
        '''
        res = []

        i, j = 0, 0
        while i < len(fl) and j < len(sl):
            # Determine the intersection interval
            start = max(fl[i][0], sl[j][0])
            end = min(fl[i][1], sl[j][1])

            # Check if there's an intersection
            if start <= end:
                res.append([start, end])

            # Move to the next interval with the smallest endpoint
            if fl[i][1] < sl[j][1]:
                i += 1
            else:
                j += 1

        return res
        