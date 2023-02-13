class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        min=None
        for i in self.stack:
            if min ==None or i< min:
                min=i
        return min