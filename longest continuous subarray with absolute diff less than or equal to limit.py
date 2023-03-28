def longestSubarray(nums: list[int], limit: int) -> int:
        l,r=0,0
        max_=nums[0]
        min_=nums[0]
        while r<len(nums):
            max_=max(nums[r], max_)
            min_=min(nums[r], max_)
            if nums[r]>max_:max_=nums[r]
            elif nums[l]<min_:min_=nums[l]
            if abs(max_-min_)<=limit:
                r+=1
            elif abs(max_-min_)>limit:
                if max_==nums[l]:
                    max_=nums[l+1]
                l+=1
        return r-l
longestSubarray([8,2,4,7], 4)