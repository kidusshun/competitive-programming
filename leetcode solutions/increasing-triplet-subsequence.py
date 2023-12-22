class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = nums[0]
        biggest = nums[-1]
        bigs = []
        for i in range(len(nums)-2,-1,-1):
            biggest = max(biggest,nums[i+1])
            bigs.append(biggest)
        bigs.reverse()
        for i in range(1, len(nums)-1):
            if smallest < nums[i] < bigs[i]:
                return True
            smallest = min(smallest,nums[i])
        return False

