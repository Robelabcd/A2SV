class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(60*int(t[:2]) + int(t[3:]) for t in timePoints)
        
        diff = minutes[0] - minutes[-1] + 24 * 60
        for i in range(len(minutes)-1):
            diff = min(diff, minutes[i+1] - minutes[i])
            
        return diff