class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        lasttime = 0
        cur = 0
        for processor in processorTime:
            lasttime = max(processor + tasks[cur], lasttime)
            cur += 4
        return lasttime
        