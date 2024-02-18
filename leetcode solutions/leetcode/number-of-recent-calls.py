class RecentCounter:

    def __init__(self):
        self.recent = deque()

    def ping(self, t: int) -> int:
        self.recent.append(t)
        while not t-3000<= self.recent[0] <= t:
            self.recent.popleft()
        return len(self.recent)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)