class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=[-1]*k
        self.front=0
        self.rear=0
        self.size=0
        self.k=k

    def insertFront(self, value: int) -> bool:
        if self.isFull():return False
        if self.isEmpty():
            self.queue[self.front]=value
        else:
            self.front =(self.front-1) % self.k
            self.queue[self.front]=value
        self.size+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():return False
        if self.isEmpty():self.queue[self.rear]=value
        else:
            self.rear=(self.rear+1) % self.k
            self.queue[self.rear]=value
        self.size+=1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():return False
        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():return False
        self.queue[self.rear] = -1
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True
    def getFront(self) -> int:
        return self.queue[self.front]

    def getRear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size==self.k:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()