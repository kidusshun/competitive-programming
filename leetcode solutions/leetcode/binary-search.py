class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l<=r:
            ind = (l + r)//2
            if nums[ind] == target:
                return ind
            elif nums[ind] < target:
                l = ind+1
            else:
                r = ind -1
        return -1