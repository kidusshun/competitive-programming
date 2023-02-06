class MyQueue:

    def __init__(self):
        self.stack_1=[]
        self.stack_2=[]

    def push(self, x: int) -> None:
        self.stack_1.append(x)
    def pop(self) -> int:
        if len(self.stack_2)==0:
            while(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    def peek(self) -> int:
        if len(self.stack_2)==0:
            while(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2[len(self.stack_2)-1]

    def empty(self) -> bool:
        if len(self.stack_1)==0 and len(self.stack_2)==0:
            return True
        else:
            return False
