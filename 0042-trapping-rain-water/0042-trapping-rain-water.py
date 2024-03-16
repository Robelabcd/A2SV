class Solution:
    def trap(self, height: List[int]) -> int:
        
        '''
        '''
        #precompute the forward max
        temp_max = 0
        Forwardmax = []
        for i in range(len(height)):
            temp_max = max(temp_max, height[i])
            Forwardmax.append(temp_max)

        #Precompute the backward max
        temp_max = 0
        Backmax = []
        for i in range(len(height)-1, -1, -1):
            temp_max = max(temp_max, height[i])
            Backmax.append(temp_max)
        Backmax.reverse()
        

        minn = []
        for i in range(len(height)):
            temp = min(Forwardmax[i], Backmax[i])
            minn.append(temp)

        #Jump 0 at front
        i = 0
        while i < len(height):
            if height[i] == 0:
                i += 1
            else:
                break

        output = 0
        while i < len(height):

            trapped_water = minn[i] - height[i]

            if trapped_water > 0:

                output += trapped_water

            i += 1

        return output






















