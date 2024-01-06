class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        triplets = []
        for fixed in range(length):
            if fixed > 0 and nums[fixed] == nums[fixed-1]:
                continue
            i,j = fixed+1, length-1
            while i<j:
                curr_sum = nums[i]+nums[fixed]+nums[j]
                if curr_sum == 0:
                    lst = sorted([nums[i], nums[j], nums[fixed]])
                    triplets.append(lst)
                    i+=1
                    while nums[i] == nums[i-1] and i<j:
                        i+=1
                elif curr_sum < 0:
                    i+=1
                elif curr_sum > 0:
                    j-=1
        return triplets
