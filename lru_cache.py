class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=ListNode(0,0)
        self.tail=ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1
    

    def put(self, key: int, value: int) -> None: 
        if key in self.cache:    
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            node.value = value
        else: 
            if len(self.cache) >= self.capacity:
                self.remove_from_tail()
            node = ListNode(key,value)
            self.cache[key] = node
            self.add(node)
    
    def add(self, node):
        head_next=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=head_next
        head_next.prev=node
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def remove_from_tail(self):
        if len(self.cache)==0: return
        tail_node =self.tail.prev
        del self.cache[tail_node.key]
        self.remove(tail_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)