import heapq

class Solution:
    def getOrder(self, tasks):
        
        indexed_tasks = [] 
        for i, (start, duration) in enumerate(tasks):
            indexed_tasks.append((start, duration, i))
        
        indexed_tasks.sort()
        
        result, heap = [], []    
        time = i = 0  
        while heap or i < len(indexed_tasks):
            
            if not heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]

            
            while i < len(indexed_tasks) and indexed_tasks[i][0] <= time:
                start, duration, index = indexed_tasks[i]
                heapq.heappush(heap, (duration, index))
                i += 1


            if heap:
                duration, index = heapq.heappop(heap)
                time += duration  # Increment current time by the task's duration
                result.append(index) 
        return result

