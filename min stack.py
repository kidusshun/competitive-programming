class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')
        
    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        self.min =min(self.min, val)

    def pop(self) -> None:
        self.min = self.stack[-1][1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min







print(min(2,3))
min=MinStack()
min.push(2)
min.push(3)
min.push(5)
min.push(5)
min.push(6)
min.push(1)
min.getMin()
min.pop()
min.getMin()
