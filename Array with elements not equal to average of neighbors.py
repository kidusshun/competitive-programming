class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)-1):
            prev=nums[i-1]
            current=nums[i]
            next=nums[i+1]
            if prev<current<next or next>current>prev:
                nums[i+1], nums[i] = nums[i], nums[i+1]
        return nums