class FrequencyTracker:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.tracker[number]]-=1  
        self.tracker[number] +=1
        self.freq[self.tracker[number]]+=1

    def deleteOne(self, number: int) -> None:
        if number in self.tracker.keys():
            self.freq[self.tracker[number]]-=1
            self.tracker[number] -=1
            self.freq[self.tracker[number]]+=1
            if self.tracker[number] == 0:
                del self.tracker[number]

    def hasFrequency(self, frequency: int) -> bool:
        if self.freq[frequency] == 0: return False
        return True

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)