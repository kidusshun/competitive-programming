class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapify(nums)
        self.k = k
        while len(self.nums) > self.k:
            heappop(self.nums)        

    def add(self, val: int) -> int:
        heappush(self.nums,val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]