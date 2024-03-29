class MyCalendar:

    def __init__(self):
        self.calendar = {}

    def book(self, start: int, end: int) -> bool:
        if len(self.calendar) == 0:
            self.calendar[start] = end
            return True
        else:
            arr = list(self.calendar.keys())
            ind = self.binary(arr, start)

            if arr[ind] <= start < self.calendar[arr[ind]] or arr[ind+1] <= end <= self.calendar[arr[ind+1]] :
                return False
            else:
                self.calendar[start] = end
                self.calendar = dict(sorted(self.calendar.items()))
                return True

    
    def binary(self, arr, start):
        l,r = 0, len(arr) - 1

        while l<=r:
            mid = (l+r)//2
            if arr[mid] < start:
                l= mid + 1
            elif arr[mid] > start:
                r= mid - 1
            else:
                return arr[mid]
        if mid == 0:return mid
        return mid - 1
        

s = MyCalendar()
print(s.book(47, 50))
print(s.book(33, 41))
print(s.book(39, 45))
print(s.book(33, 42))
print(s.book(25, 32))
print(s.book(26, 35))
print(s.book(19, 25))
print(s.book(3, 8))
print(s.book(8, 13))
print(s.book(18, 27))
[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = print(obj.book(start,end))