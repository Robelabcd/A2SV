class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        difference = t - 3000
        queue.append(t)
        while(queue and queue[0] < difference):
            queue.popleft()
        return len(queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)