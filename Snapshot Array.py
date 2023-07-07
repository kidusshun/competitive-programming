class SnapshotArray:
    def binary(self, l,r, target, lst):
        ans = 0

        while l <= r:
            mid = (l+r)//2
            if lst[mid][1] <=target:
                ans = mid
                l = mid +1
            else:
                r= mid - 1
        return ans

    def __init__(self, length: int):
        self.arr = [0] * length
        self.snap_id = 0
        self.nums=[[(0,0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.arr[index]=val
        if self.nums[index][-1][1]==self.snap_id:
            self.nums[index][-1]=(val,self.snap_id)
        elif self.nums[index][-1][1]<self.snap_id:
            self.nums[index].append((val,self.snap_id))
        

    def snap(self) -> int:
        val = self.snap_id
        self.snap_id += 1
        return val

    def get(self, index: int, snap_id: int) -> int:
        x=self.binary(0,len(self.nums[index])-1,snap_id,self.nums[index])
        return self.nums[index][x][0]

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)