class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*n
        self.n = n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        ans = []
        while self.pointer<self.n:
            if self.stream[self.pointer]:
                ans.append(self.stream[self.pointer])
            else:
                break
            self.pointer +=1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)