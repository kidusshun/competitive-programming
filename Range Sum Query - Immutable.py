class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]*len(self.nums)
        
        self.prefix[0] = self.nums[0]
        for i in range(1,len(self.nums)):
            self.prefix[i] = self.prefix[i-1] +self.nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]
        