class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.length+=1

    def findMedian(self) -> float:
        self.arr.sort()
        if self.length%2 !=0:
            return self.arr[self.length//2]
        median = (self.arr[self.length//2] + self.arr[(self.length//2) - 1])/2
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()