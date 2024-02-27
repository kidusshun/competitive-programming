class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i= 0
        count = 0
        for i in range(len(nums)-2):
            curr = nums[i]
            l,r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r] > curr:
                    count += r-l
                    l+=1
                else:
                    r-=1
        return count
        